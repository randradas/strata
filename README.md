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
sdd init my-app                 # prompts for profile, name, description, stack
sdd init . -y --name X          # no prompts, full profile
sdd init app --profile minimal  # small scaffold: product doc, specs, skills
sdd profiles                    # list profiles
sdd spec new "User login"       # specs/001-user-login/{spec,plan,tasks}.md
sdd spec list                   # ids + status
```

## Generated layout (`full` profile)

```
CLAUDE.md                 # short map, hard rules
.sdd.toml                 # records profile and sdd version
docs/                     # product, architecture, conventions, glossary, ADRs
specs/README.md           # workflow and lifecycle
specs/_template/          # spec/plan/tasks templates (edit freely)
.claude/skills/           # spec, plan, tasks, implement
```

`minimal` keeps `CLAUDE.md`, `docs/product.md`, `specs/` and all skills.

## Develop

```sh
uv run pytest
```

Templates live in `src/sdd_init/templates/<layer>/` (`base`, `full`, `minimal`). Profiles pick layers in
`src/sdd_init/profiles.py`. Prefix `dot-` becomes `.` on output.
