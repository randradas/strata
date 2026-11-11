from pathlib import Path

import pytest

from strata_sdd.cli import main


def init(tmp_path: Path, *extra: str) -> int:
    return main(["init", str(tmp_path), "-y", "--name", "Demo", "--description", "A demo app", *extra])


def test_init_writes_skeleton(tmp_path):
    assert init(tmp_path) == 0
    claude = (tmp_path / "CLAUDE.md").read_text()
    assert "# Demo" in claude and "A demo app" in claude
    assert (tmp_path / ".claude/skills/spec/SKILL.md").exists()
    assert (tmp_path / "docs/product.md").exists()
    # spec template placeholders survive init untouched
    assert "{{spec_id}}" in (tmp_path / "specs/_template/spec.md").read_text()


def test_init_refuses_overwrite(tmp_path, capsys):
    (tmp_path / "CLAUDE.md").write_text("mine")
    assert init(tmp_path) == 1
    assert "CLAUDE.md" in capsys.readouterr().err
    assert (tmp_path / "CLAUDE.md").read_text() == "mine"
    assert init(tmp_path, "--force") == 0


def test_spec_new_numbers_and_renders(tmp_path):
    init(tmp_path)
    assert main(["spec", "new", "User Login!", "--root", str(tmp_path)]) == 0
    assert main(["spec", "new", "Export CSV", "--root", str(tmp_path)]) == 0
    first = tmp_path / "specs/001-user-login"
    assert sorted(p.name for p in first.iterdir()) == ["plan.md", "spec.md", "tasks.md"]
    spec = (first / "spec.md").read_text()
    assert "id: 001-user-login" in spec and "{{" not in spec
    assert (tmp_path / "specs/002-export-csv").is_dir()


def test_spec_list(tmp_path, capsys):
    init(tmp_path)
    main(["spec", "new", "Login", "--root", str(tmp_path)])
    capsys.readouterr()
    main(["spec", "list", "--root", str(tmp_path)])
    assert "001-login" in capsys.readouterr().out


def test_spec_new_without_init(tmp_path):
    assert main(["spec", "new", "X", "--root", str(tmp_path)]) == 1
