#!/usr/bin/env python3

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "github-launch-kit"
SKILL_MD = SKILL_DIR / "SKILL.md"
OPENAI_YAML = SKILL_DIR / "agents" / "openai.yaml"


def fail(message: str) -> int:
    print(message)
    return 1


def main() -> int:
    if not SKILL_MD.exists():
        return fail("Missing github-launch-kit/SKILL.md")
    if not OPENAI_YAML.exists():
        return fail("Missing github-launch-kit/agents/openai.yaml")

    skill_text = SKILL_MD.read_text(encoding="utf-8")
    frontmatter = re.match(r"^---\n(.*?)\n---", skill_text, re.DOTALL)
    if not frontmatter:
        return fail("SKILL.md is missing YAML frontmatter")

    frontmatter_text = frontmatter.group(1)
    if "name: github-launch-kit" not in frontmatter_text:
        return fail("SKILL.md frontmatter must include name: github-launch-kit")
    if "description:" not in frontmatter_text:
        return fail("SKILL.md frontmatter must include description")

    openai_text = OPENAI_YAML.read_text(encoding="utf-8")
    if "$github-launch-kit" not in openai_text:
        return fail("openai.yaml must reference $github-launch-kit in default_prompt")

    print("Skill files look valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
