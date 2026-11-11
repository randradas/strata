<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/logo/strata-lockup-on-dark.svg">
  <img src="assets/logo/strata-lockup-on-light.svg" alt="strata" width="234">
</picture>

# strata

> strata: layered specs and context for AI coding agents.

Scaffold projects for **spec driven development** with **progressive disclosure** docs, tuned for Claude Code.

- Root `CLAUDE.md` stays short: a map, not a manual.
- Detail lives in `docs/` and `specs/`, read only when a task needs it.
- Claude Code skills drive the flow: `/spec` -> `/plan` -> `/tasks` -> `/implement`.

## Install

```sh
uv tool install git+https://github.com/randradas/strata.git   # puts `strata` on PATH
uvx --from git+https://github.com/randradas/strata.git strata init my-app   # or run once, no install
```

From a local clone: `uv tool install --editable .`

## Use

```sh
strata init my-app                 # prompts for profile, name, description, stack
strata init . -y --name X          # no prompts, full profile
strata init app --profile minimal  # small scaffold: product doc, specs, skills
strata profiles                    # list profiles
strata spec new "User login"       # specs/001-user-login/{spec,plan,tasks}.md
strata spec list                   # ids + status
```

## Generated layout (`full` profile)

```
CLAUDE.md                 # short map, hard rules
.strata.toml              # records profile and strata version
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

Templates live in `src/strata_sdd/templates/<layer>/` (`base`, `full`, `minimal`). Profiles pick layers in
`src/strata_sdd/profiles.py`. Prefix `dot-` becomes `.` on output.

## License

strata is MIT licensed, see [`LICENSE`](LICENSE).

Files `strata` writes into your project are yours: no strata notice to keep
([`LICENSE-GENERATED.md`](LICENSE-GENERATED.md)). Exception: the `grill` skill adapts text from
Matt Pocock's skills and ships with its own MIT license file; keep it with the skill.
