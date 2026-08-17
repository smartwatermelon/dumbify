#!/usr/bin/env python3
"""Sanity-check SKILL.md structure and the plugin/marketplace manifests."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_PATH = ROOT / "SKILL.md"


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    if not SKILL_PATH.exists():
        fail("SKILL.md not found")

    text = SKILL_PATH.read_text(encoding="utf-8")

    frontmatter_match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if frontmatter_match is None:
        fail("SKILL.md must start with YAML frontmatter")
    frontmatter = frontmatter_match.group(1)

    for required_key in ("name:", "description:"):
        if not re.search(rf"(?m)^{re.escape(required_key)}", frontmatter):
            key = required_key[:-1]
            fail(f"SKILL.md frontmatter missing required key: {key}")

    for nonportable_key in ("compatibility:", "allowed-tools:"):
        if re.search(rf"(?m)^{re.escape(nonportable_key)}", frontmatter):
            key = nonportable_key[:-1]
            fail(f"Remove nonportable frontmatter key: {key}")

    manifests = {}
    for manifest_name in ("plugin.json", "marketplace.json"):
        manifest_path = ROOT / ".claude-plugin" / manifest_name
        try:
            manifests[manifest_name] = json.loads(
                manifest_path.read_text(encoding="utf-8")
            )
        except FileNotFoundError:
            fail(f"{manifest_name} not found")
        except json.JSONDecodeError as exc:
            fail(f"{manifest_name} is not valid JSON: {exc}")

    skill_version_match = re.search(
        r"(?m)^\s*version:\s*[\"']?([^\"'\n]+)", frontmatter
    )
    if skill_version_match is None:
        fail("SKILL.md frontmatter missing metadata.version")
    skill_version = skill_version_match.group(1).strip()
    plugin_version = manifests["plugin.json"].get("version")
    if skill_version != plugin_version:
        fail(
            "Version mismatch: SKILL.md metadata.version="
            f"{skill_version!r} vs. plugin.json version={plugin_version!r}"
        )

    print("SKILL.md and plugin manifests are valid")


if __name__ == "__main__":
    main()
