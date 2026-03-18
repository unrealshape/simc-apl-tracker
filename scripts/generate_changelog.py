#!/usr/bin/env python3
"""Generate changelogs per class/spec from synced APL diffs."""

import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHANGELOG_DIR = ROOT / "changelog"
CHANGES_FILE = CHANGELOG_DIR / ".last_sync_changes.json"

CLASSES = [
    "deathknight", "demonhunter", "druid", "evoker", "hunter", "mage",
    "monk", "paladin", "priest", "rogue", "shaman", "warlock", "warrior",
]


def get_changed_files() -> list[str]:
    """Read list of changed files from last sync."""
    if not CHANGES_FILE.exists():
        return []
    return json.loads(CHANGES_FILE.read_text())


def classify_changes(files: list[str]) -> dict[str, list[str]]:
    """Group changed files by class."""
    by_class: dict[str, list[str]] = {}
    for f in files:
        for cls in CLASSES:
            if f"/{cls}/" in f or f"_{cls}_" in f.lower() or f"_{cls}." in f.lower():
                by_class.setdefault(cls, []).append(f)
                break
    return by_class


def get_git_diff(filepath: str) -> str:
    """Get git diff for a file, returns empty string if not in git yet."""
    full_path = ROOT / filepath
    try:
        result = subprocess.run(
            ["git", "diff", "--no-color", "--", str(full_path)],
            capture_output=True, text=True, cwd=ROOT
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout
        # Try diff for untracked files
        result = subprocess.run(
            ["git", "diff", "--no-color", "--no-index", "/dev/null", str(full_path)],
            capture_output=True, text=True, cwd=ROOT
        )
        return result.stdout if result.returncode in (0, 1) else ""
    except FileNotFoundError:
        return ""


def extract_apl_changes(diff_text: str) -> list[str]:
    """Extract meaningful APL action changes from a diff."""
    changes = []
    for line in diff_text.splitlines():
        if line.startswith("+") and not line.startswith("+++"):
            content = line[1:].strip()
            if content and not content.startswith("#"):
                changes.append(f"  + `{content}`")
        elif line.startswith("-") and not line.startswith("---"):
            content = line[1:].strip()
            if content and not content.startswith("#"):
                changes.append(f"  - `{content}`")
    return changes


def generate_changelog(changed_by_class: dict[str, list[str]]) -> str:
    """Generate markdown changelog content."""
    now = datetime.now(timezone.utc)
    lines = [
        f"# APL Changelog – {now.strftime('%Y-%m-%d')}",
        "",
        f"Generated: {now.strftime('%Y-%m-%d %H:%M UTC')}",
        "",
    ]

    for cls in sorted(changed_by_class.keys()):
        lines.append(f"## {cls.replace('_', ' ').title()}")
        lines.append("")
        for filepath in sorted(changed_by_class[cls]):
            spec = Path(filepath).stem
            lines.append(f"### {spec.replace('_', ' ').title()}")
            lines.append(f"File: `{filepath}`")
            lines.append("")
            diff = get_git_diff(filepath)
            if diff:
                changes = extract_apl_changes(diff)
                if changes:
                    lines.append("Changes:")
                    lines.extend(changes[:50])  # Limit to 50 lines
                    if len(changes) > 50:
                        lines.append(f"  ... and {len(changes) - 50} more changes")
                else:
                    lines.append("Minor formatting/metadata changes.")
            else:
                lines.append("New file added.")
            lines.append("")
        lines.append("")

    return "\n".join(lines)


def main() -> int:
    changed_files = get_changed_files()
    if not changed_files:
        print("No changes to generate changelog for.")
        return 0

    # Only APL files, not profiles
    apl_files = [f for f in changed_files if f.startswith("apl/")]
    if not apl_files:
        print("No APL changes to log.")
        return 0

    changed_by_class = classify_changes(apl_files)
    if not changed_by_class:
        print("No class-specific changes found.")
        return 0

    print(f"Generating changelog for {len(changed_by_class)} classes...")
    changelog = generate_changelog(changed_by_class)

    # Write dated changelog
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    out_file = CHANGELOG_DIR / f"{today}.md"
    out_file.write_text(changelog, encoding="utf-8")
    print(f"Written: {out_file.relative_to(ROOT)}")

    # Also write latest.md for easy access
    latest = CHANGELOG_DIR / "latest.md"
    latest.write_text(changelog, encoding="utf-8")
    print(f"Written: {latest.relative_to(ROOT)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
