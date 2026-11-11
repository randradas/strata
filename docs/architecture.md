# Architecture

Stack: Python 3.12, stdlib only (argparse, importlib.resources), uv + uv_build, pytest

## Components

- `src/sdd_init/cli.py` - argparse entry point (`sdd`). Parses args, prompts, prints. No file logic.
- `src/sdd_init/scaffold.py` - all file logic: template walk, rendering, spec numbering, spec listing.
- `src/sdd_init/templates/project/` - files shipped by `sdd init`, mirrored 1:1 into the target.
- `tests/` - pytest, drives the CLI through `main(argv)` against `tmp_path`.

## Data flow

`sdd init <path>`:
1. `cli.cmd_init` builds a `ProjectContext` from flags, then prompts (skipped with `-y` or no TTY).
2. `scaffold.init_project` walks `templates/project/`, maps names, checks for clashes, renders, writes.

`sdd spec new <title>`:
1. `scaffold.new_spec` reads the **target project's** `specs/_template/` (not the package templates),
   so each project can customise its own spec templates.
2. Next number = max existing `NNN-` prefix + 1. Slug from title.

## Template rules

- Placeholders: `{{key}}`. Unknown keys are left untouched, so a template can carry
  placeholders meant for a later stage (e.g. `{{spec_id}}` survives `init`, filled by `spec new`).
- Init keys: `project_name`, `description`, `stack`, `date`. Spec keys: `spec_id`, `title`, `spec_date`.
- Path mapping: a `dot-` prefix becomes `.` (hidden dirs survive packaging); `.tmpl` suffix is stripped.

## Boundaries and constraints

- No runtime dependencies.
- Never overwrite user files without `--force`; clash check runs before any write.
