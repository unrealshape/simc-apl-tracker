#!/usr/bin/env python3
"""Sync APL files from SimulationCraft repo and store them structured by class/spec."""

import json
import os
import sys
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError

SIMC_REPO = "simulationcraft/simc"
BRANCH = "thewarwithin"
API_BASE = f"https://api.github.com/repos/{SIMC_REPO}"
RAW_BASE = f"https://raw.githubusercontent.com/{SIMC_REPO}/{BRANCH}"
ROOT = Path(__file__).resolve().parent.parent

CLASSES = [
    "deathknight", "demonhunter", "druid", "evoker", "hunter", "mage",
    "monk", "paladin", "priest", "rogue", "shaman", "warlock", "warrior",
]

APL_SOURCES = {
    "default": "ActionPriorityLists/default",
    "assisted_combat": "ActionPriorityLists/assisted_combat",
}

PROFILE_PATH = "profiles"


def api_get(endpoint: str) -> dict | list:
    """GitHub API call (used only for directory listings)."""
    url = f"{API_BASE}/{endpoint}"
    headers = {"Accept": "application/vnd.github+json"}
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = Request(url, headers=headers)
    with urlopen(req) as resp:
        return json.loads(resp.read())


def raw_download(path: str) -> str:
    """Download file via raw.githubusercontent.com (no rate limit)."""
    url = f"{RAW_BASE}/{path}"
    req = Request(url)
    with urlopen(req) as resp:
        return resp.read().decode("utf-8")


def get_tree(path: str) -> list[dict]:
    """Get directory listing from GitHub API."""
    try:
        return api_get(f"contents/{path}?ref={BRANCH}")
    except HTTPError as e:
        if e.code == 404:
            return []
        raise


def parse_class_spec(filename: str) -> tuple[str, str] | None:
    """Extract class and spec from filename like 'warrior_arms.simc'."""
    name = filename.removesuffix(".simc").removesuffix(".txt")
    name = name.lower()
    for cls in CLASSES:
        if name.startswith(cls + "_"):
            spec = name[len(cls) + 1:]
            if spec:
                return cls, spec
    return None


def sync_apl_directory(source_key: str, remote_path: str) -> list[str]:
    """Sync one APL directory (default or assisted_combat)."""
    changed = []
    entries = get_tree(remote_path)
    if not entries:
        print(f"  No files found at {remote_path}")
        return changed

    for entry in entries:
        if entry["type"] != "file":
            continue
        fname = entry["name"]
        parsed = parse_class_spec(fname)
        if not parsed:
            continue
        cls, spec = parsed

        content = raw_download(f"{remote_path}/{fname}")
        out_dir = ROOT / "apl" / source_key / cls
        out_dir.mkdir(parents=True, exist_ok=True)
        out_file = out_dir / f"{spec}.simc"

        old_content = out_file.read_text(encoding="utf-8") if out_file.exists() else ""
        if content != old_content:
            out_file.write_text(content, encoding="utf-8")
            changed.append(f"apl/{source_key}/{cls}/{spec}.simc")
            print(f"  Updated: {cls}/{spec}")
        else:
            print(f"  Unchanged: {cls}/{spec}")

    return changed


def sync_profiles() -> list[str]:
    """Sync profile .simc files from profiles/ directory tree."""
    changed = []
    entries = get_tree(PROFILE_PATH)
    if not entries:
        return changed

    for tier_entry in entries:
        if tier_entry["type"] != "dir" or not tier_entry["name"].startswith("TWW"):
            continue
        tier = tier_entry["name"]
        tier_files = get_tree(f"{PROFILE_PATH}/{tier}")
        for f in tier_files:
            if f["type"] != "file" or not f["name"].endswith(".simc"):
                continue
            content = raw_download(f"{PROFILE_PATH}/{tier}/{f['name']}")
            out_dir = ROOT / "profiles" / tier
            out_dir.mkdir(parents=True, exist_ok=True)
            out_file = out_dir / f["name"]

            old = out_file.read_text(encoding="utf-8") if out_file.exists() else ""
            if content != old:
                out_file.write_text(content, encoding="utf-8")
                changed.append(f"profiles/{tier}/{f['name']}")

    return changed


def main() -> int:
    print("=== SimC APL Sync ===")
    all_changed = []

    for key, remote in APL_SOURCES.items():
        print(f"\nSyncing {key} APLs from {remote}/...")
        changed = sync_apl_directory(key, remote)
        all_changed.extend(changed)

    print(f"\nSyncing profiles...")
    all_changed.extend(sync_profiles())

    print(f"\n{'='*40}")
    print(f"Total files changed: {len(all_changed)}")
    for f in all_changed:
        print(f"  {f}")

    # Write changed files list for downstream scripts
    manifest = ROOT / "changelog" / ".last_sync_changes.json"
    manifest.parent.mkdir(parents=True, exist_ok=True)
    manifest.write_text(json.dumps(all_changed, indent=2) + "\n")

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except HTTPError as e:
        print(f"GitHub API error: {e.code} {e.reason}", file=sys.stderr)
        sys.exit(1)
