# sdd-init

CLI (`sdd`) that scaffolds projects for spec driven development with progressive disclosure docs, tuned for Claude Code.

Stack: Python 3.12, stdlib only (argparse, importlib.resources), uv + uv_build, pytest

This repo is built with its own tool: specs here drive changes to `sdd`.

## How we work

Spec driven. No code without an approved spec.
Flow: `/spec` -> `/plan` -> `/tasks` -> `/implement`. Details: `specs/README.md`.

## Two kinds of template (do not mix them up)

| Path | What it is | Change it when |
|---|---|---|
| `src/sdd_init/templates/` (layers) | **Product.** Files `sdd init` ships to users. | A spec changes what users get. |
| `CLAUDE.md`, `docs/`, `specs/`, `.claude/` | **This repo's own process.** | We change how we build `sdd`. |

A fix to the shipped templates is NOT a fix to this repo's copies, and the reverse. If both should change, say so in the plan.

## Where to look (read only what the task needs)

| Need | Read |
|---|---|
| Why the tool exists, users, goals | `docs/product.md` |
| Modules, template layout, rendering | `docs/architecture.md` |
| Code style, testing, commits | `docs/conventions.md` |
| Domain terms | `docs/glossary.md` |
| Past decisions | `docs/decisions/` |
| Known pain points, backlog ideas | `docs/friction.md` |
| Feature work, past and current | `specs/NNN-*/` |

Full doc index: `docs/README.md`.

## Hard rules

- Do not change a spec marked `status: approved` without asking.
- Tick tasks in `tasks.md` as you finish them.
- Write an ADR in `docs/decisions/` only for decisions that are hard to reverse, surprising, and a real trade-off.
- Keep runtime dependencies at zero unless an ADR says otherwise.
- Run `uv run pytest` before calling a task done.
- Hit friction using `sdd` or its skills? Add a line to `docs/friction.md`, keep going.
