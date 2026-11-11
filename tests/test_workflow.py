"""Content checks for spec 005: skills and templates carry each workflow rule.

These prove the rules are written down, not that Claude follows them (see 005 plan, D23).
"""

from pathlib import Path

import pytest

from strata_sdd.cli import main
from strata_sdd.scaffold import TEMPLATES

REPO = Path(__file__).resolve().parent.parent


@pytest.fixture(scope="module")
def project(tmp_path_factory) -> Path:
    root = tmp_path_factory.mktemp("full")
    assert main(["init", str(root), "-y", "--name", "Demo"]) == 0
    return root


def read(project: Path, rel: str) -> str:
    return (project / rel).read_text().lower()


def skill(project: Path, name: str) -> str:
    return read(project, f".claude/skills/{name}/SKILL.md")


def has_all(text: str, *phrases: str) -> None:
    missing = [p for p in phrases if p.lower() not in text]
    assert missing == []


# AC1
def test_grill_asks_in_rounds(project):
    has_all(skill(project, "grill"), "round", "number", "recommended answer", '"yes" accepts', "look up")


def test_spec_creates_first_then_grills(project):
    text = skill(project, "spec")
    has_all(text, "strata spec new", "grill")
    assert text.index("strata spec new") < text.index("grill")


# AC2
def test_grill_writes_decisions_at_once(project):
    has_all(skill(project, "grill"), "## decisions", "next `d` id", "at once")


# AC3
def test_grill_stop_rule(project):
    has_all(skill(project, "grill"), '"enough"', "open questions")


# AC4
def test_spec_template_ids_and_decisions(project):
    has_all(read(project, "specs/_template/spec.md"), "- [ ] ac1:", "## decisions", "d1:")


# AC5
def test_readme_freeze_rule(project):
    has_all(read(project, "specs/README.md"), "renumber", "frozen", "struck out", "never reused")


# AC6
def test_plan_grills_and_writes_draft(project):
    has_all(skill(project, "plan"), "grill", "continue", "status: draft")
    has_all(read(project, "specs/_template/plan.md"), "status: draft", "## decisions")


# AC7
def test_tasks_refuses_unapproved_plan(project):
    has_all(skill(project, "tasks"), "status: approved", "stop")


# AC8
def test_tasks_need_ac_ids(project):
    has_all(skill(project, "tasks"), "ac ids")
    has_all(read(project, "specs/_template/tasks.md"), "(ac1)")


# AC9
def test_commit_rules(project):
    has_all(read(project, "specs/README.md"), "## commits", "<spec id>: <task number> <summary>", "approved", "never push")
    for name in ("spec", "plan", "implement"):
        has_all(skill(project, name), "specs/readme.md", "commit")


# AC10
def test_implement_without_git(project):
    has_all(skill(project, "implement"), "not a git repo", "skip", "once", "git init")


# AC11
def test_grill_updates_glossary(project):
    has_all(skill(project, "grill"), "docs/glossary.md", "clash")


# AC12
def test_adr_three_part_test(project):
    for name in ("grill", "plan"):
        has_all(skill(project, name), "hard to reverse", "surprising", "trade-off")


# AC13
def test_grill_asks_before_creating(project):
    has_all(skill(project, "grill"), "ask", "before creating", "claude.md", "do not ask again")


# AC14
def test_glossary_and_adr_formats(project):
    has_all(read(project, "docs/glossary.md"), "_avoid_:")
    adr = read(project, "docs/decisions/README.md")
    has_all(adr, "status:", "date:", "1-3 sentences", "optional")
    assert "## context" not in adr


# AC15
def test_grill_credit_and_license(project):
    text = skill(project, "grill")
    assert "matt pocock" in text.strip().splitlines()[-1]
    has_all(read(project, ".claude/skills/grill/LICENSE-mattpocock-skills.md"), "mit license", "matt pocock")


# D21: repo process copies must equal shipped templates
SHARED = {
    "base/dot-claude/skills": ".claude/skills",
    "base/specs/_template": "specs/_template",
    "base/specs/README.md": "specs/README.md",
    "full/docs/decisions/README.md": "docs/decisions/README.md",
}


def _files(path: Path) -> dict[str, bytes]:
    if path.is_file():
        return {"": path.read_bytes()}
    return {p.relative_to(path).as_posix(): p.read_bytes() for p in sorted(path.rglob("*")) if p.is_file()}


@pytest.mark.parametrize("shipped,repo", SHARED.items())
def test_repo_copies_match_shipped(shipped, repo):
    assert _files(Path(str(TEMPLATES / shipped))) == _files(REPO / repo)
