# Friction log

Pain points found while building `sdd` with `sdd`. Log them when hit; do not fix on the spot.
Newest first. When an entry becomes a spec, fill the Spec column.

| Date | Friction | Spec |
|---|---|---|
| 2026-11-11 | After editing skills mid-session, re-invoking `/spec` loaded the old cached text; had to read the skill file by hand. Skill edits need a new session (or a manual read) to take effect. | - |
| 2026-11-11 | Headless smoke run of `/spec` proves only round 1; later rounds, decision writing and approval commits need a human in the loop. | - |
| 2026-11-11 | No skill covers the friction log; entries are written by hand outside the workflow. | - |
| 2026-11-11 | No skill covers ADRs; they are written by hand outside the workflow. | 005 |
| 2026-11-11 | `/plan` asks for approval but has nowhere to record it (see plan-status entry); skill and template should agree. | 005 |
| 2026-11-11 | `/implement` never says to commit; per-task commits in 004 were ad hoc, not part of the skill. | 005 |
| 2026-11-11 | Spec acceptance criteria have no ids, so `tasks.md` for 004 had to restate them as AC1-AC10 to map tasks and tests. | 005 |
| 2026-11-11 | Workflow says "human approves the plan" but `plan.md` has no status field; approval of 004 plan lives only in chat. | 005 |
| 2026-11-11 | Spec template has no home for answered open questions. Drafting 004 needed a hand-added "Decisions" section. | 005 |
| 2026-11-11 | `spec new` assumes a new feature. Recording already-built features (reverse specs 001-003) needed hand-written `plan.md`/`tasks.md` and manual `status: done`. Same wall for anyone adopting SDD on existing code. | - |

## Spec candidates

Ideas for the next specs. Each one links to the friction it answers, if any.

| Idea | Answers | Spec |
|---|---|---|
| Reverse specs / `strata init --existing`: adopt SDD on a repo that already has code, record built features without hand edits. | `spec new` assumes a new feature | - |
| Friction-log skill: log a pain point in one step, from any session. | No skill covers the friction log | - |
| `strata check`: lint a project for leftover TODOs, a growing root agent file, specs stuck in draft, ACs no task covers. Good for CI. | (none yet; idea) | - |
