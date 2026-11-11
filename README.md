# sdd-init

Scaffold projects for **spec driven development** with **progressive disclosure** docs, tuned for Claude Code.

- Root `CLAUDE.md` stays short: a map, not a manual.
- Detail lives in `docs/` and `specs/`, read only when a task needs it.
- Claude Code skills drive the flow: `/spec` -> `/plan` -> `/tasks` -> `/implement`.

## Install

```sh
uv tool install --editable .   # puts `sdd` on PATH
```

## Use

```sh
sdd init my-app                 # prompts for name, description, stack
sdd init . -y --name X          # no prompts
sdd spec new "User login"       # specs/001-user-login/{spec,plan,tasks}.md
sdd spec list                   # ids + status
```

## Generated layout

```
CLAUDE.md                 # short map, hard rules
docs/                     # product, architecture, conventions, glossary, ADRs
specs/README.md           # workflow and lifecycle
specs/_template/          # spec/plan/tasks templates (edit freely)
.claude/skills/           # spec, plan, tasks, implement
```

## Develop

```sh
uv run pytest
```

Templates live in `src/sdd_init/templates/project/`. Prefix `dot-` becomes `.` on output.
