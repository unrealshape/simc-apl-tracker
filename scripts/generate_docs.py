#!/usr/bin/env python3
"""Generate Markdown documentation per spec from synced APL files."""

import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APL_DIR = ROOT / "apl" / "default"
DOCS_DIR = ROOT / "docs"

CLASSES = [
    "deathknight", "demonhunter", "druid", "evoker", "hunter", "mage",
    "monk", "paladin", "priest", "rogue", "shaman", "warlock", "warrior",
]

CLASS_DISPLAY = {
    "deathknight": "Death Knight",
    "demonhunter": "Demon Hunter",
    "druid": "Druid",
    "evoker": "Evoker",
    "hunter": "Hunter",
    "mage": "Mage",
    "monk": "Monk",
    "paladin": "Paladin",
    "priest": "Priest",
    "rogue": "Rogue",
    "shaman": "Shaman",
    "warlock": "Warlock",
    "warrior": "Warrior",
}


def parse_apl_file(filepath: Path) -> list[dict]:
    """Parse a .simc APL file into structured action blocks."""
    blocks = []
    current_list = None

    for line in filepath.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        # Match action list headers: actions.precombat=... or actions.default=...
        m = re.match(r"^actions\.?(\w*)[\+]?=/?(.*)$", line)
        if not m:
            # Also match: actions+=/...
            m = re.match(r"^actions[\+]?=/?(.*)$", line)
            if m:
                current_list = "default"
                action_str = m.group(1)
            else:
                continue
        else:
            list_name = m.group(1) or "default"
            action_str = m.group(2)
            if list_name != current_list:
                current_list = list_name

        if not action_str:
            continue

        # Parse action: name,if=condition,target=...
        parts = action_str.split(",", 1)
        action_name = parts[0].strip()
        conditions = parts[1].strip() if len(parts) > 1 else ""

        blocks.append({
            "list": current_list,
            "action": action_name,
            "conditions": conditions,
            "raw": line,
        })

    return blocks


def generate_spec_doc(cls: str, spec: str, apl_file: Path) -> str:
    """Generate markdown documentation for a single spec."""
    display_class = CLASS_DISPLAY.get(cls, cls.title())
    display_spec = spec.replace("_", " ").title()
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    blocks = parse_apl_file(apl_file)

    # Group by action list
    lists: dict[str, list[dict]] = {}
    for b in blocks:
        lists.setdefault(b["list"], []).append(b)

    lines = [
        f"# {display_class} – {display_spec}",
        "",
        f"Auto-generated from SimulationCraft APL | Last updated: {now}",
        "",
        f"Source: `apl/default/{cls}/{spec}.simc`",
        "",
        "---",
        "",
    ]

    # Summary
    lines.append("## Overview")
    lines.append("")
    lines.append(f"- **Action Lists:** {len(lists)}")
    lines.append(f"- **Total Actions:** {len(blocks)}")
    action_list_names = ", ".join(f"`{name}`" for name in lists.keys())
    lines.append(f"- **Lists:** {action_list_names}")
    lines.append("")

    # Each action list
    for list_name, actions in lists.items():
        lines.append(f"## Action List: `{list_name}`")
        lines.append("")
        lines.append(f"| # | Action | Conditions |")
        lines.append(f"|---|--------|------------|")
        for i, a in enumerate(actions, 1):
            cond = a["conditions"].replace("|", "\\|") if a["conditions"] else "—"
            lines.append(f"| {i} | `{a['action']}` | {cond} |")
        lines.append("")

    # Raw APL
    lines.append("## Raw APL")
    lines.append("")
    lines.append("```")
    lines.append(apl_file.read_text(encoding="utf-8").strip())
    lines.append("```")
    lines.append("")

    return "\n".join(lines)


def main() -> int:
    print("=== Generating Spec Documentation ===")
    count = 0

    for cls in CLASSES:
        cls_dir = APL_DIR / cls
        if not cls_dir.exists():
            continue

        for apl_file in sorted(cls_dir.glob("*.simc")):
            spec = apl_file.stem
            doc = generate_spec_doc(cls, spec, apl_file)

            out_dir = DOCS_DIR / cls
            out_dir.mkdir(parents=True, exist_ok=True)
            out_file = out_dir / f"{spec}.md"
            out_file.write_text(doc, encoding="utf-8")
            print(f"  {cls}/{spec}.md")
            count += 1

    print(f"\nGenerated {count} spec documents.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
