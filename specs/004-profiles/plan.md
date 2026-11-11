# Plan: Profiles

Spec: `spec.md` (approved). Plan approved 2026-11-11 (in chat; see friction log).

## Approach

Split shipped templates into **layers**. A profile is an ordered list of layers; files from later
layers override same-path files from earlier ones. See ADR 0002.

```
templates/
  base/      shared by all profiles: docs/product.md, specs/**, dot-claude/skills/**, dot-sdd.toml
  full/      CLAUDE.md (full map), docs/README.md, architecture, conventions, glossary, decisions/
  minimal/   CLAUDE.md (short map: product doc + specs only)
```

- `full` = `base + full`. `minimal` = `base + minimal`.
- Each profile has its own `CLAUDE.md`, so a minimal project never points to missing docs.
  No conditional logic in templates; renderer stays `{{key}}` only.
- Profile registry in a new `profiles.py`: name -> description + layers. Single source for CLI
  validation, prompt choices and `sdd profiles` output.
- Record the profile in `.sdd.toml` (from `base/dot-sdd.toml`), with `profile` and `sdd_version`.
  Read back with stdlib `tomllib` when a later command needs it (not needed in this spec).
- Skills that read optional docs (plan, implement) say "if it exists, else skip".

CLI:
- `sdd init --profile NAME`. Validated against the registry (not argparse `choices`, which exits 2;
  spec needs exit 1 + list of valid names).
- Interactive init with no flag: prompt `Profile (minimal, full) [full]`.
- New `sdd profiles` command: one line per profile, `name  description`.

## Changes

| Area / file | Change |
|---|---|
| `src/sdd_init/templates/project/` | Move into `templates/base/`, `templates/full/`, `templates/minimal/` (git mv, keep history). |
| `templates/minimal/CLAUDE.md` | New: short map, links only `docs/product.md` and `specs/`. |
| `templates/base/dot-sdd.toml` | New: `profile = "{{profile}}"`, `sdd_version = "{{sdd_version}}"`. |
| `templates/base/dot-claude/skills/{plan,implement}/SKILL.md` | Optional docs worded "if it exists". |
| `src/sdd_init/profiles.py` | New: `Profile` dataclass, `PROFILES` dict, `get_profile(name)` raising `ValueError` with valid names. |
| `src/sdd_init/scaffold.py` | `init_project(target, ctx, profile, force)`: merge layers (later wins), then existing clash check + write. `ProjectContext` gains `profile`; vars gain `profile`, `sdd_version`. |
| `src/sdd_init/cli.py` | `--profile` flag + prompt; `ValueError` -> stderr, exit 1; new `profiles` subcommand. |
| `tests/test_cli.py` | Tests per acceptance criterion (below). |
| `docs/architecture.md` | Update Components and Template rules for layers and profiles. |
| `.sdd.toml` (repo process) | Add `profile = "full"` so this repo matches what `sdd init` now writes. |
| `README.md` | Document `--profile` and `sdd profiles`. |

## Risks and mitigations

- **Two `CLAUDE.md` files drift apart.** Test: for each profile, every backticked repo path in the
  generated `CLAUDE.md` must exist in the output. Catches dangling links in both.
- **Default behaviour changes by accident.** Test: `init` with no profile == `--profile full`, file
  set identical to v0.1 plus `.sdd.toml`.
- **Layer override hides a mistake** (file in two layers by accident). Only `CLAUDE.md` is allowed to
  overlap; test asserts no other overlaps.
- **Existing projects lack `.sdd.toml`.** Fine for now; future readers must treat missing as `full`.
  Noted in ADR.

## Test strategy

| Acceptance criterion | Test |
|---|---|
| No profile -> full, unchanged | file set equals `--profile full`; contains all v0.1 files |
| minimal -> only listed files | exact file set for minimal |
| skills skip missing docs | plan/implement SKILL.md contain "if it exists" wording |
| minimal CLAUDE.md no dangling links | backticked paths in CLAUDE.md exist (both profiles) |
| full == no profile | covered by first test |
| interactive prompt, default full | feed stdin with monkeypatched `isatty` + `input` returning "" |
| unknown profile -> nothing written, names listed, exit 1 | dir empty after; stderr has `minimal` and `full` |
| profile list | `sdd profiles` output has each name + description |
| spec new works in minimal | init minimal, `spec new`, three files created |
| profile recorded | `.sdd.toml` parsed with `tomllib`, `profile` matches |
