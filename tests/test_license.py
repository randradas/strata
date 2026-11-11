"""Spec 007: strata is MIT; files it writes into a target project belong to the user."""

import tomllib
from pathlib import Path

import pytest

from strata_sdd import __version__
from strata_sdd.cli import main

REPO = Path(__file__).resolve().parent.parent
GRILL_LICENSE = "src/strata_sdd/templates/base/dot-claude/skills/grill/LICENSE-mattpocock-skills.md"

MIT = """\
MIT License

Copyright (c) 2026 Roberto Andradas Izquierdo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


def read(path: str) -> str:
    return (REPO / path).read_text()


def flat(text: str) -> str:
    return " ".join(text.lower().split())


def pyproject() -> dict:
    return tomllib.loads(read("pyproject.toml"))["project"]


# AC1
def test_license_is_standard_mit():
    assert read("LICENSE") == MIT


# AC2
def test_statement_gives_generated_files_to_user():
    text = flat(read("LICENSE-GENERATED.md"))
    assert "are yours" in text
    assert "need not keep strata's copyright or license notice" in text


# AC3
def test_statement_keeps_third_party_notice():
    text = flat(read("LICENSE-GENERATED.md"))
    assert "keeps its own license and notice" in text
    assert "grill" in text and "license-mattpocock-skills.md" in text


# AC4
def test_package_declares_mit_and_ships_license_files():
    project = pyproject()
    assert project["license"] == "MIT"
    assert project["license-files"] == ["LICENSE", "LICENSE-GENERATED.md", GRILL_LICENSE]
    for path in project["license-files"]:
        assert (REPO / path).is_file(), path


# AC5
def test_version_is_042():
    assert pyproject()["version"] == __version__ == "0.4.2"


# AC6
def test_readme_has_license_section():
    readme = read("README.md")
    assert "\n## License\n" in readme
    section = flat(readme.split("\n## License\n", 1)[1].split("\n## ", 1)[0])
    for needle in ("mit", "license-generated.md", "yours", "grill"):
        assert needle in section, needle


# AC7
@pytest.mark.parametrize("profile", ["minimal", "full"])
def test_init_writes_no_strata_license(tmp_path, profile):
    assert main(["init", str(tmp_path), "-y", "--name", "Demo", "--profile", profile]) == 0
    assert not [p.name for p in tmp_path.iterdir() if p.name.upper().startswith(("LICENSE", "NOTICE"))]
    assert (tmp_path / ".claude/skills/grill/LICENSE-mattpocock-skills.md").is_file()
