#!/usr/bin/env python3
"""Check SimulationCraft repo for new APL-relevant commits."""

import json
import os
import sys
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError

SIMC_REPO = "simulationcraft/simc"
BRANCH = "thewarwithin"
API_BASE = f"https://api.github.com/repos/{SIMC_REPO}"
LAST_COMMIT_FILE = Path(__file__).resolve().parent.parent / "changelog" / ".last_simc_commit"

APL_PATHS = (
    "ActionPriorityLists/",
    "engine/class_modules/",
    "profiles/",
)


def gh_output(key: str, value: str) -> None:
    """Write to $GITHUB_OUTPUT if running in Actions, else print."""
    gh_out = os.environ.get("GITHUB_OUTPUT")
    if gh_out:
        with open(gh_out, "a") as f:
            f.write(f"{key}={value}\n")
    print(f"  >> {key}={value}")


def api_get(endpoint: str) -> dict | list:
    url = f"{API_BASE}/{endpoint}"
    headers = {"Accept": "application/vnd.github+json"}
    token = os.environ.get("GH_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = Request(url, headers=headers)
    with urlopen(req) as resp:
        return json.loads(resp.read())


def get_latest_commit_sha() -> str:
    data = api_get(f"commits?sha={BRANCH}&per_page=1")
    return data[0]["sha"]


def get_last_known_sha() -> str | None:
    if LAST_COMMIT_FILE.exists():
        sha = LAST_COMMIT_FILE.read_text().strip()
        return sha if sha else None
    return None


def get_commits_since(since_sha: str) -> list[dict]:
    commits = api_get(f"commits?sha={BRANCH}&per_page=100")
    new_commits = []
    for c in commits:
        if c["sha"] == since_sha:
            break
        new_commits.append(c)
    return new_commits


def commit_touches_apl(sha: str) -> bool:
    data = api_get(f"commits/{sha}")
    for f in data.get("files", []):
        if any(f["filename"].startswith(p) for p in APL_PATHS):
            return True
    return False


def save_last_commit(sha: str) -> None:
    LAST_COMMIT_FILE.parent.mkdir(parents=True, exist_ok=True)
    LAST_COMMIT_FILE.write_text(sha + "\n")


def write_summary(apl_commits: list[dict], latest_sha: str) -> None:
    """Write Job Summary for GitHub Actions."""
    summary_file = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary_file:
        return
    lines = [
        "## APL Tracker – Nightly Check",
        "",
        f"**SimC Branch:** `{BRANCH}`",
        f"**Latest Commit:** [`{latest_sha[:12]}`](https://github.com/{SIMC_REPO}/commit/{latest_sha})",
        f"**APL-relevant Commits:** {len(apl_commits)}",
        "",
    ]
    if apl_commits:
        lines.append("| Commit | Message |")
        lines.append("|--------|---------|")
        for c in apl_commits:
            sha_short = c["sha"][:12]
            msg = c["commit"]["message"].split("\n")[0]
            lines.append(f"| [`{sha_short}`](https://github.com/{SIMC_REPO}/commit/{c['sha']}) | {msg} |")
    with open(summary_file, "a") as f:
        f.write("\n".join(lines) + "\n")


def main() -> int:
    dry_run = "--dry-run" in sys.argv

    latest_sha = get_latest_commit_sha()
    last_known = get_last_known_sha()

    print(f"SimC branch: {BRANCH}")
    print(f"Latest commit: {latest_sha[:12]}")
    print(f"Last known:    {last_known[:12] if last_known else 'none'}")

    if last_known == latest_sha:
        print("No new commits.")
        gh_output("new_commits", "false")
        return 0

    if last_known is None:
        print("First run – full sync needed.")
        if not dry_run:
            save_last_commit(latest_sha)
        gh_output("new_commits", "true")
        gh_output("latest_sha", latest_sha)
        gh_output("apl_commits", "0")
        gh_output("summary", "First run – full sync")
        return 0

    new_commits = get_commits_since(last_known)
    print(f"New commits: {len(new_commits)}")

    apl_commits = []
    for c in new_commits:
        if commit_touches_apl(c["sha"]):
            short = c["sha"][:12]
            msg = c["commit"]["message"].split("\n")[0]
            print(f"  APL-relevant: {short} {msg}")
            apl_commits.append(c)

    if not apl_commits:
        print("No APL-relevant changes.")
        if not dry_run:
            save_last_commit(latest_sha)
        gh_output("new_commits", "false")
        return 0

    print(f"APL-relevant commits: {len(apl_commits)}")
    if not dry_run:
        save_last_commit(latest_sha)

    # Collect changed classes from commit messages/files
    changed_classes = set()
    for c in apl_commits:
        data = api_get(f"commits/{c['sha']}")
        for f in data.get("files", []):
            for cls_name in ["deathknight", "demonhunter", "druid", "evoker",
                             "hunter", "mage", "monk", "paladin", "priest",
                             "rogue", "shaman", "warlock", "warrior"]:
                if cls_name in f["filename"].lower():
                    changed_classes.add(cls_name)

    gh_output("new_commits", "true")
    gh_output("latest_sha", latest_sha)
    gh_output("apl_commits", str(len(apl_commits)))
    gh_output("changed_classes", ",".join(sorted(changed_classes)))
    gh_output("summary", f"{len(apl_commits)} APL commits – {', '.join(sorted(changed_classes))}")

    write_summary(apl_commits, latest_sha)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except HTTPError as e:
        print(f"GitHub API error: {e.code} {e.reason}", file=sys.stderr)
        sys.exit(1)
