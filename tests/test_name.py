"""Spec 006: the tool is `strata`; `sdd` survives only as history and as the method "SDD"."""

import re
import tomllib
from pathlib import Path

import pytest

from strata_sdd import __version__
from strata_sdd.cli import build_parser, main

REPO = Path(__file__).resolve().parent.parent
TAGLINE = "strata: layered specs and context for AI coding agents."

# Lowercase `sdd` as its own word, or the old package/module/config names.
# "SDD" (the method) and `strata-sdd` / `strata_sdd` (the package) are allowed.
OLD_NAME = re.compile(r"(?<![\w-])sdd(?![\w-])|sdd[-_]init|\.sdd\.toml")


def old_name_hits(root: Path, paths) -> list[str]:
    hits = []
    for path in paths:
        for n, line in enumerate(path.read_text().splitlines(), 1):
            if OLD_NAME.search(line) and not line.startswith("_Avoid_:"):
                hits.append(f"{path.relative_to(root)}:{n}: {line.strip()}")
    return hits


def pyproject() -> dict:
    return tomllib.loads((REPO / "pyproject.toml").read_text())["project"]


# AC1
def test_cli_is_named_strata(capsys):
    assert build_parser().prog == "strata"
    with pytest.raises(SystemExit):
        main(["--version"])
    assert capsys.readouterr().out.strip() == f"strata {__version__}"


# AC2, AC3
def test_package_metadata():
    project = pyproject()
    assert project["name"] == "strata-sdd"
    assert project["version"] == __version__ == "0.4.1"
    assert project["description"] == TAGLINE
    assert project["scripts"] == {"strata": "strata_sdd.cli:main"}


# AC4
@pytest.mark.parametrize("profile", ["minimal", "full"])
def test_generated_project_never_names_sdd(tmp_path, profile):
    assert main(["init", str(tmp_path), "-y", "--name", "Demo", "--profile", profile]) == 0
    files = [p for p in tmp_path.rglob("*") if p.is_file()]
    assert old_name_hits(tmp_path, files) == []


# AC5
def test_config_file_named_after_strata(tmp_path):
    main(["init", str(tmp_path), "-y"])
    assert not (tmp_path / ".sdd.toml").exists()
    config = tomllib.loads((tmp_path / ".strata.toml").read_text())
    assert config == {"profile": "full", "strata_version": __version__}


# AC6: repo process files, skipping history (D10, D11)
HISTORY = {
    "docs/decisions/0001-self-host-with-sdd.md",
    "docs/decisions/0002-layered-templates-for-profiles.md",
}


def repo_process_files() -> list[Path]:
    files = [REPO / "CLAUDE.md", REPO / "README.md", REPO / "pyproject.toml", REPO / ".strata.toml"]
    files += sorted((REPO / "docs").rglob("*.md"))
    files += sorted((REPO / ".claude").rglob("*.md"))
    files += sorted((REPO / "specs/_template").glob("*.md")) + [REPO / "specs/README.md"]
    files += sorted((REPO / "src").rglob("*.py"))
    return [
        f for f in files
        if f.relative_to(REPO).as_posix() not in HISTORY and f.name != "friction.md"
    ]


def test_repo_process_files_never_name_sdd():
    assert old_name_hits(REPO, repo_process_files()) == []


def test_friction_candidates_use_new_name():
    text = (REPO / "docs/friction.md").read_text()
    candidates = text[text.index("## Spec candidates"):]
    assert not OLD_NAME.search(candidates)


def test_glossary_defines_method_and_tool():
    text = (REPO / "docs/glossary.md").read_text()
    assert "**SDD**:" in text and "**strata**:" in text
