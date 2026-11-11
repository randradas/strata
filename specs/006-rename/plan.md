---
status: approved
---

# Plan: Rename

Spec: `spec.md` (must be `approved` before this is filled). Decision ids continue from the spec.

## Approach

A mechanical rename, guarded by tests that scan for the old name.

1. `git mv` the code folder (`src/sdd_init` -> `src/strata_sdd`) and the config template
   (`dot-sdd.toml` -> `dot-strata.toml`) to keep history (D13).
2. Package metadata: name `strata-sdd`, version 0.4.0, tagline as description, one script `strata`.
3. Code: module paths, CLI program name, help and messages, error text.
4. Shipped templates: the `/spec` skill and `specs/README.md` say `strata spec new`; config comment says `strata`.
5. Tests first: name-scan tests (D12) plus package metadata and CLI name tests; then existing tests move to the new module.
6. This repo: `.sdd.toml` -> `.strata.toml`, root agent file, README, docs, glossary paths, friction candidates (D11),
   repo skill copies via the drift test. Relock and resync so the local `sdd` script disappears.
7. After merge (D7): give the user commands to rename the folder, uninstall the global `sdd-init` tool
   (installed now, v0.3.0) and install `strata-sdd` from the new folder.

## Decisions

Settled while grilling the plan. Newest last.

- D11: Friction log entries keep their original wording; new entries and the "Spec candidates" ideas use `strata`.
- D12: Tests fail if any generated file, in either profile, contains `sdd` as a lowercase word; "SDD" (the method) is allowed. Same scan for this repo's process files, skipping history (D10, D11).
- D13: Moves use `git mv` so `git log --follow` keeps file history.

## Changes

| Area / file | Change |
|---|---|
| `src/sdd_init/` -> `src/strata_sdd/` | `git mv`; `files("strata_sdd")`; CLI `prog="strata"`, messages, docstrings. |
| `templates/base/dot-sdd.toml` -> `dot-strata.toml` | `git mv`; comment names `strata`. |
| `templates/base/dot-claude/skills/spec/SKILL.md`, `templates/base/specs/README.md` | `strata spec new`. |
| `pyproject.toml` | `strata-sdd`, 0.4.0, tagline, `strata = "strata_sdd.cli:main"`. |
| `tests/*` | Import `strata_sdd`; `.strata.toml`; new `tests/test_name.py`. |
| Repo: `.sdd.toml` -> `.strata.toml`, `CLAUDE.md`, `README.md`, `docs/{README,product,architecture,glossary}.md`, friction candidates | New name, tagline; history untouched. |
| Repo skills, `specs/README.md` | Copied from shipped (drift test). |
| `uv.lock`, `.venv` | Relock, sync. |

## Risks and mitigations

- **A leftover `sdd` somewhere.** Name-scan tests over generated output and repo process files.
- **Old global install still answers `sdd`.** It is v0.3.0 from `uv tool`; the post-merge commands uninstall it.
- **Session paths break when the folder moves.** Folder rename happens last, by the user (D7).
- **History files edited by mistake.** AC8 check: `git diff main` on specs 001-005 and ADRs 0001-0002 is empty.

## Test strategy

| AC | Check |
|---|---|
| AC1 | `main(["--version"])` and help output say `strata`; existing command tests pass on the new module. |
| AC2 | Package scripts are exactly `{"strata": ...}`; after sync, no `sdd` in `.venv/bin`. |
| AC3 | `pyproject.toml` parsed: name, version 0.4.0, description = tagline; wheel builds as `strata_sdd-0.4.0`. |
| AC4 | Name scan over generated `full` and `minimal` projects. |
| AC5 | `.strata.toml` exists with profile and version; no `.sdd.toml`. |
| AC6 | Name scan over repo process files (history skipped); glossary has **SDD** and **strata**. |
| AC7 | Commands given in the final message; checked by the user. |
| AC8 | `git diff main` on history files is empty. |
