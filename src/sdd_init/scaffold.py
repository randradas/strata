"""Render bundled templates into a target directory."""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date
from importlib.resources import files
from importlib.resources.abc import Traversable
from pathlib import Path

TEMPLATES = files("sdd_init") / "templates"
PLACEHOLDER = re.compile(r"\{\{\s*(\w+)\s*\}\}")
SPEC_DIR = re.compile(r"^(\d{3})-")


@dataclass
class ProjectContext:
    name: str
    description: str
    stack: str

    def as_vars(self) -> dict[str, str]:
        return {
            "project_name": self.name,
            "description": self.description,
            "stack": self.stack,
            "date": date.today().isoformat(),
        }


def render(text: str, variables: dict[str, str]) -> str:
    """Replace {{key}} placeholders. Unknown keys stay as-is."""
    return PLACEHOLDER.sub(lambda m: variables.get(m.group(1), m.group(0)), text)


def _walk(node: Traversable, rel: Path = Path()):
    for child in sorted(node.iterdir(), key=lambda c: c.name):
        if child.is_dir():
            yield from _walk(child, rel / child.name)
        else:
            yield rel / child.name, child


def _target_name(rel: Path) -> Path:
    # Templates use "dot-" prefix so hidden dirs survive packaging.
    parts = [("." + p[4:]) if p.startswith("dot-") else p for p in rel.parts]
    path = Path(*parts)
    return path.with_suffix("") if path.suffix == ".tmpl" else path


def init_project(target: Path, ctx: ProjectContext, force: bool = False) -> list[Path]:
    """Write the project skeleton. Return written paths (relative)."""
    variables = ctx.as_vars()
    planned = [(_target_name(rel), src) for rel, src in _walk(TEMPLATES / "project")]

    if not force:
        clashes = [rel for rel, _ in planned if (target / rel).exists()]
        if clashes:
            listing = "\n  ".join(str(c) for c in clashes)
            raise FileExistsError(f"Refusing to overwrite (use --force):\n  {listing}")

    written = []
    for rel, src in planned:
        dest = target / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(render(src.read_text(encoding="utf-8"), variables), encoding="utf-8")
        written.append(rel)
    return written


def slugify(title: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return slug or "spec"


def next_spec_number(specs_dir: Path) -> int:
    numbers = [
        int(m.group(1))
        for p in specs_dir.iterdir()
        if p.is_dir() and (m := SPEC_DIR.match(p.name))
    ] if specs_dir.exists() else []
    return max(numbers, default=0) + 1


def new_spec(root: Path, title: str) -> Path:
    """Create specs/NNN-slug/ from the project's own templates."""
    specs_dir = root / "specs"
    template_dir = specs_dir / "_template"
    if not template_dir.is_dir():
        raise FileNotFoundError(f"No {template_dir} found. Run `sdd init` first.")

    spec_id = f"{next_spec_number(specs_dir):03d}-{slugify(title)}"
    dest = specs_dir / spec_id
    dest.mkdir()
    variables = {"spec_id": spec_id, "title": title, "spec_date": date.today().isoformat()}
    for src in sorted(template_dir.glob("*.md")):
        (dest / src.name).write_text(render(src.read_text(encoding="utf-8"), variables), encoding="utf-8")
    return dest


def list_specs(root: Path) -> list[tuple[str, str]]:
    """Return (spec_id, status) for each spec."""
    specs_dir = root / "specs"
    if not specs_dir.exists():
        return []
    out = []
    for p in sorted(specs_dir.iterdir()):
        if not (p.is_dir() and SPEC_DIR.match(p.name)):
            continue
        status = "unknown"
        spec_file = p / "spec.md"
        if spec_file.exists():
            m = re.search(r"^status:\s*(\S+)", spec_file.read_text(encoding="utf-8"), re.M)
            if m:
                status = m.group(1)
        out.append((p.name, status))
    return out
