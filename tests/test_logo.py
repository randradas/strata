"""Spec 008: strata has a logo in the repo, shown in the README, never shipped to targets."""

import xml.etree.ElementTree as ET
from pathlib import Path

import pytest

from strata_sdd.cli import main

REPO = Path(__file__).resolve().parent.parent
LOGO = REPO / "assets/logo"
SVG_NS = "{http://www.w3.org/2000/svg}"

ACCENT = "#e8743b"
LIGHT = {ACCENT, "#6b7385", "#14171f"}  # D1: on light ground
DARK = {ACCENT, "#8c95a6", "#f2f3f5"}  # D1: on dark ground

FILES = {
    "strata-mark.svg": LIGHT | DARK,  # D10: switches with the theme
    "strata-icon.svg": LIGHT | DARK,
    "strata-lockup-on-light.svg": LIGHT,
    "strata-lockup-on-dark.svg": DARK,
}
LOCKUPS = ["strata-lockup-on-light.svg", "strata-lockup-on-dark.svg"]


def svg(name: str) -> str:
    return (LOGO / name).read_text().lower()


# AC1
@pytest.mark.parametrize("name", FILES)
def test_logo_file_is_svg(name):
    root = ET.parse(LOGO / name).getroot()
    assert root.tag == f"{SVG_NS}svg"
    assert root.get("viewBox")


# AC2
@pytest.mark.parametrize("name, colors", FILES.items())
def test_logo_uses_d1_colors(name, colors):
    text = svg(name)
    for color in colors:
        assert color in text, color


def test_lockups_stay_on_their_ground():
    assert "#f2f3f5" not in svg("strata-lockup-on-light.svg")
    assert "#14171f" not in svg("strata-lockup-on-dark.svg")


@pytest.mark.parametrize("name", ["strata-mark.svg", "strata-icon.svg"])
def test_mark_switches_with_theme(name):
    assert "prefers-color-scheme: dark" in svg(name)


# AC5
@pytest.mark.parametrize("name", LOCKUPS)
def test_wordmark_is_outlined(name):
    root = ET.parse(LOGO / name).getroot()
    assert root.find(f".//{SVG_NS}text") is None
    assert root.find(f".//{SVG_NS}path") is not None
    text = svg(name)
    assert "font-family" not in text and "@font-face" not in text


# AC3, AC4
def test_readme_shows_logo_by_theme():
    readme = (REPO / "README.md").read_text()
    head = readme.split("\n# strata\n", 1)[0]
    assert "<picture>" in head
    assert '<source media="(prefers-color-scheme: dark)" srcset="assets/logo/strata-lockup-on-dark.svg">' in head
    assert 'src="assets/logo/strata-lockup-on-light.svg"' in head
    assert 'alt="strata"' in head


# AC7
@pytest.mark.parametrize("profile", ["minimal", "full"])
def test_init_writes_no_logo(tmp_path, profile):
    assert main(["init", str(tmp_path), "-y", "--name", "Demo", "--profile", profile]) == 0
    assert not list(tmp_path.rglob("*.svg"))


# AC8
def test_logo_under_repo_mit_license():
    assert (REPO / "LICENSE").read_text().startswith("MIT License\n")
    assert not [p for p in (REPO / "assets").rglob("*") if p.name.upper().startswith(("LICENSE", "NOTICE"))]
