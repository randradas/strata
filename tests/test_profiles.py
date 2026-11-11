import re
import tomllib
from pathlib import Path

import pytest

from strata_sdd import __version__, cli
from strata_sdd.cli import main

V01_FILES = {
    "CLAUDE.md",
    "docs/README.md",
    "docs/architecture.md",
    "docs/conventions.md",
    "docs/decisions/README.md",
    "docs/glossary.md",
    "docs/product.md",
    ".claude/skills/implement/SKILL.md",
    ".claude/skills/plan/SKILL.md",
    ".claude/skills/spec/SKILL.md",
    ".claude/skills/tasks/SKILL.md",
    "specs/README.md",
    "specs/_template/plan.md",
    "specs/_template/spec.md",
    "specs/_template/tasks.md",
}
GRILL_FILES = {".claude/skills/grill/SKILL.md", ".claude/skills/grill/LICENSE-mattpocock-skills.md"}
FULL_FILES = V01_FILES | GRILL_FILES | {".strata.toml"}
MINIMAL_FILES = {
    "CLAUDE.md",
    "docs/product.md",
    ".claude/skills/implement/SKILL.md",
    ".claude/skills/plan/SKILL.md",
    ".claude/skills/spec/SKILL.md",
    ".claude/skills/tasks/SKILL.md",
    "specs/README.md",
    "specs/_template/plan.md",
    "specs/_template/spec.md",
    "specs/_template/tasks.md",
    ".strata.toml",
} | GRILL_FILES


def init(path: Path, *extra: str) -> int:
    return main(["init", str(path), "-y", "--name", "Demo", *extra])


def files_in(root: Path) -> set[str]:
    return {p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file()}


# AC1, AC5
def test_default_profile_is_full_and_matches_v01(tmp_path):
    default, full = tmp_path / "default", tmp_path / "full"
    assert init(default) == 0
    assert init(full, "--profile", "full") == 0
    assert files_in(default) == files_in(full) == FULL_FILES


# AC2
def test_minimal_file_set(tmp_path):
    assert init(tmp_path, "--profile", "minimal") == 0
    assert files_in(tmp_path) == MINIMAL_FILES


# AC3
def test_skills_tolerate_missing_docs(tmp_path):
    init(tmp_path, "--profile", "minimal")
    for skill in ("plan", "implement"):
        text = (tmp_path / f".claude/skills/{skill}/SKILL.md").read_text()
        assert "if it exists" in text


# AC4 (both profiles, guards drift between the two CLAUDE.md files)
@pytest.mark.parametrize("profile", ["minimal", "full"])
def test_claude_md_links_resolve(tmp_path, profile):
    init(tmp_path, "--profile", profile)
    text = (tmp_path / "CLAUDE.md").read_text()
    paths = [
        t for t in re.findall(r"`([^`\s]+)`", text)
        if "/" in t and not t.startswith("/") and "NNN" not in t
    ]
    assert paths, "expected CLAUDE.md to link some docs"
    missing = [p for p in paths if not (tmp_path / p).exists()]
    assert missing == []


# AC6
def test_interactive_prompts_for_profile_default_full(tmp_path, monkeypatch):
    prompts = []

    class TTY:
        def isatty(self):
            return True

    monkeypatch.setattr(cli.sys, "stdin", TTY())
    monkeypatch.setattr("builtins.input", lambda p: prompts.append(p) or "")
    assert main(["init", str(tmp_path)]) == 0
    assert any("Profile" in p and "[full]" in p for p in prompts)
    assert files_in(tmp_path) == FULL_FILES


# AC7
def test_unknown_profile_writes_nothing(tmp_path, capsys):
    assert init(tmp_path, "--profile", "huge") == 1
    err = capsys.readouterr().err
    assert "huge" in err and "minimal" in err and "full" in err
    assert files_in(tmp_path) == set()


# AC8
def test_profiles_command_lists_all(capsys):
    assert main(["profiles"]) == 0
    lines = capsys.readouterr().out.strip().splitlines()
    assert {line.split()[0] for line in lines} == {"minimal", "full"}
    assert all(len(line.split()) > 1 for line in lines), "each profile needs a description"


# AC9
def test_spec_new_in_minimal(tmp_path):
    init(tmp_path, "--profile", "minimal")
    assert main(["spec", "new", "Login", "--root", str(tmp_path)]) == 0
    assert files_in(tmp_path / "specs/001-login") == {"spec.md", "plan.md", "tasks.md"}


# AC10
@pytest.mark.parametrize("profile", ["minimal", "full"])
def test_profile_recorded(tmp_path, profile):
    init(tmp_path, "--profile", profile)
    config = tomllib.loads((tmp_path / ".strata.toml").read_text())
    assert config == {"profile": profile, "strata_version": __version__}


# ADR 0002: only CLAUDE.md may live in more than one layer
def test_layers_only_overlap_on_claude_md():
    from strata_sdd.scaffold import TEMPLATES, _walk

    seen: dict[str, int] = {}
    for layer in TEMPLATES.iterdir():
        if layer.is_dir():
            for rel, _ in _walk(layer):
                seen[rel.as_posix()] = seen.get(rel.as_posix(), 0) + 1
    assert {path for path, n in seen.items() if n > 1} == {"CLAUDE.md"}
