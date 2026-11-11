# Specs

Each feature lives in `specs/NNN-slug/` with three files:

1. `spec.md` - **what** and **why**. Decisions, acceptance criteria. No tech choices.
2. `plan.md` - **how**. Design, decisions, files touched, risks. Written after the spec is approved.
3. `tasks.md` - ordered checklist. Each task small, testable, and names the acceptance criteria it covers.

## Lifecycle

`spec.md` front matter `status:` moves through `draft` -> `approved` -> `in-progress` -> `done`.
`plan.md` front matter `status:` moves through `draft` -> `approved`.

- `/spec` and `/plan` grill the user (`grill` skill) until no decision is open.
- Human approves the spec before planning, and the plan before tasks.
- Open questions go in `## Open questions`, never guessed.

## Ids

- Decisions: `D1`, `D2`... unique per spec folder; `plan.md` continues from the spec's last id.
- Acceptance criteria: `AC1`, `AC2`... Tasks: `T1`, `T2`...
- While `draft`, renumber freely. Once `approved`, ids are frozen: a dropped item stays, struck out
  (`~~AC3: ...~~ dropped`), and its id is never reused.

## Commits

- Approving a spec or plan: commit `<spec id>: approve spec` / `<spec id>: approve plan`.
- Each finished task, after tests pass: commit `<spec id>: <task number> <summary>`.
- Never push; that is the user's call.
- Not a git repo: skip commits.

## Create one

```sh
strata spec new "Feature title"
```

Or in Claude Code: `/spec Feature title`.
Templates live in `specs/_template/`. Edit them to fit your team.
