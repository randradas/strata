# Specs

Each feature lives in `specs/NNN-slug/` with three files:

1. `spec.md` - **what** and **why**. User stories, acceptance criteria. No tech choices.
2. `plan.md` - **how**. Design, files touched, risks. Written after spec is approved.
3. `tasks.md` - ordered checklist. Each task small and testable.

## Lifecycle

`status:` in `spec.md` front matter moves through:

`draft` -> `approved` -> `in-progress` -> `done`

- Human approves the spec before planning.
- Human approves the plan before tasks run.
- Open questions go in `spec.md` under "Open questions", never guessed.

## Create one

```sh
sdd spec new "Feature title"
```

Or in Claude Code: `/spec Feature title`.
Templates live in `specs/_template/`. Edit them to fit your team.
