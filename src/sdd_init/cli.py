"""`sdd` command line entry point."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import __version__
from .profiles import DEFAULT_PROFILE, get_profile
from .scaffold import ProjectContext, init_project, list_specs, new_spec


def ask(prompt: str, default: str, interactive: bool) -> str:
    if not interactive:
        return default
    answer = input(f"{prompt} [{default}]: ").strip()
    return answer or default


def cmd_init(args: argparse.Namespace) -> int:
    target = Path(args.path).resolve()
    interactive = not args.yes and sys.stdin.isatty()

    profile = args.profile or DEFAULT_PROFILE
    try:
        get_profile(profile)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 1

    ctx = ProjectContext(
        name=args.name or ask("Project name", target.name, interactive),
        description=args.description or ask("One-line description", "TODO: describe the project", interactive),
        stack=args.stack or ask("Tech stack", "TODO: list languages, frameworks, infra", interactive),
        profile=profile,
    )

    try:
        written = init_project(target, ctx, force=args.force)
    except FileExistsError as exc:
        print(exc, file=sys.stderr)
        return 1

    print(f"Scaffolded {len(written)} files in {target}")
    for rel in written:
        print(f"  {rel}")
    print("\nNext: fill docs/product.md, then run `sdd spec new \"<feature>\"` or /spec in Claude Code.")
    return 0


def cmd_spec_new(args: argparse.Namespace) -> int:
    try:
        dest = new_spec(Path(args.root).resolve(), args.title)
    except FileNotFoundError as exc:
        print(exc, file=sys.stderr)
        return 1
    print(f"Created {dest}")
    return 0


def cmd_spec_list(args: argparse.Namespace) -> int:
    specs = list_specs(Path(args.root).resolve())
    if not specs:
        print("No specs yet.")
    for spec_id, status in specs:
        print(f"{spec_id:<40} {status}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="sdd", description="Spec driven development scaffolding.")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    p_init = sub.add_parser("init", help="Scaffold a new project")
    p_init.add_argument("path", nargs="?", default=".", help="Target directory (default: .)")
    p_init.add_argument("--name", help="Project name (default: directory name)")
    p_init.add_argument("--description", help="One-line project description")
    p_init.add_argument("--stack", help="Tech stack summary")
    p_init.add_argument("--profile", help=f"Scaffold profile (default: {DEFAULT_PROFILE}); see `sdd profiles`")
    p_init.add_argument("-y", "--yes", action="store_true", help="No prompts, use defaults")
    p_init.add_argument("--force", action="store_true", help="Overwrite existing files")
    p_init.set_defaults(func=cmd_init)

    p_spec = sub.add_parser("spec", help="Work with specs")
    spec_sub = p_spec.add_subparsers(dest="spec_command", required=True)

    p_new = spec_sub.add_parser("new", help="Create a numbered spec folder")
    p_new.add_argument("title", help="Feature title")
    p_new.add_argument("--root", default=".", help="Project root (default: .)")
    p_new.set_defaults(func=cmd_spec_new)

    p_list = spec_sub.add_parser("list", help="List specs and status")
    p_list.add_argument("--root", default=".", help="Project root (default: .)")
    p_list.set_defaults(func=cmd_spec_list)

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
