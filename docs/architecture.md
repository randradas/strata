# Architecture

Stack: Python 3.12, stdlib only (argparse, importlib.resources), uv + uv_build, pytest

## Components

- `src/sdd_init/cli.py` - argparse entry point (`sdd`). Parses args, prompts, prints. No file logic.
- `src/sdd_init/scaffold.py` - all file logic: layer merge, rendering, spec numbering, spec listing.
- `src/sdd_init/profiles.py` - profile registry: name -> description + ordered layers. Single source for
  `--profile` validation, the init prompt, and `sdd profiles`.
- `src/sdd_init/templates/<layer>/` - files shipped by `sdd init`, in layers (ADR 0002):
  - `base/` - every profile: `docs/product.md`, `specs/`, skills, `.sdd.toml`.
  - `full/` - full `CLAUDE.md` map, docs index, architecture, conventions, glossary, ADRs.
  - `minimal/` - short `CLAUDE.md` that links only what `base/` creates.
- `tests/` - pytest, drives the CLI through `main(argv)` against `tmp_path`.

## Data flow

`sdd init <path>`:
1. `cli.cmd_init` resolves the profile (flag, prompt, or `full`), validates it, then builds a
   `ProjectContext` from flags and prompts (prompts skipped with `-y` or no TTY).
2. `scaffold.plan_files` merges the profile's layers in order; a later layer overrides the same path.
3. `scaffold.init_project` checks for clashes, renders, writes.

`sdd spec new <title>`:
1. `scaffold.new_spec` reads the **target project's** `specs/_template/` (not the package templates),
   so each project can customise its own spec templates.
2. Next number = max existing `NNN-` prefix + 1. Slug from title.

## Template rules

- Placeholders: `{{key}}`. Unknown keys are left untouched, so a template can carry
  placeholders meant for a later stage (e.g. `{{spec_id}}` survives `init`, filled by `spec new`).
- Only `CLAUDE.md` may exist in more than one layer (test-enforced).
- Init keys: `project_name`, `description`, `stack`, `date`, `profile`, `sdd_version`. Spec keys: `spec_id`, `title`, `spec_date`.
- Path mapping: a `dot-` prefix becomes `.` (hidden dirs survive packaging); `.tmpl` suffix is stripped.

## Boundaries and constraints

- No runtime dependencies.
- Never overwrite user files without `--force`; clash check runs before any write.
- `.sdd.toml` in a target records `profile` and `sdd_version`. Missing file = `full`, pre-0.2 project.
