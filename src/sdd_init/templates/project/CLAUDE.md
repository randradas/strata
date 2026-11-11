# {{project_name}}

{{description}}

Stack: {{stack}}

## How we work

Spec driven. No code without an approved spec.
Flow: `/spec` -> `/plan` -> `/tasks` -> `/implement`. Details: `specs/README.md`.

## Where to look (read only what the task needs)

| Need | Read |
|---|---|
| Why the product exists, users, goals | `docs/product.md` |
| System shape, modules, data flow | `docs/architecture.md` |
| Code style, testing, commits | `docs/conventions.md` |
| Domain terms | `docs/glossary.md` |
| Past decisions | `docs/decisions/` |
| Current feature work | `specs/NNN-*/` |

Full doc index: `docs/README.md`.

## Hard rules

- Do not change a spec marked `status: approved` without asking.
- Tick tasks in `tasks.md` as you finish them.
- Record new decisions as ADRs in `docs/decisions/`.
