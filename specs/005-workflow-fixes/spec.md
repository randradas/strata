---
id: 005-workflow-fixes
title: Workflow fixes
status: approved
created: 2026-11-11
---

# Workflow fixes

## Problem

Building 004 with our own workflow showed gaps (see the friction log). Specs are drafted with one
quick round of questions, so choices get made silently. Answered questions have no home. Plan
approval is not recorded. Criteria and decisions have no ids, so tasks and tests cannot point at them.
Commits and ADRs happen ad hoc. The glossary cannot list words to avoid.

## User stories

- As a developer, I want `/spec` and `/plan` to interview me until no decision is open so that nothing is silently assumed.
- As a developer, I want every decision and criterion to have an id so that plans, tasks and tests can point at them.
- As a developer, I want plan approval and per-task commits to be part of the workflow so that history shows what was approved and built.
- As a developer on a small project, I want docs to appear only when there is something real to put in them, and only with my say-so.

## Acceptance criteria

Applies to both the shipped templates and this repo's own copies (D4).

- [ ] AC1: Given `/spec`, when it runs, then it creates the spec first, then asks in rounds: every question answerable now, numbered, each with a recommended answer, worded so "yes" accepts it. Facts are looked up, not asked. (D2, D11)
- [ ] AC2: Given a grill, when a decision is settled, then it is written at once to Decisions with the next `D` id. (D11, D15)
- [ ] AC3: Given a grill, when no decision is left open or the user says "enough", then it stops; anything still open goes to Open questions. (D5)
- [ ] AC4: Given a new spec, when created, then it has a Decisions section, and acceptance criteria use `AC1`, `AC2`... ids. (D7, D15)
- [ ] AC5: Given the spec workflow guide, when read, then it states the id freeze rule: renumber freely in draft; once approved, ids are fixed, dropped items stay struck out, ids are never reused. (D7, D15)
- [ ] AC6: Given `/plan`, when it runs, then it grills design choices before writing, records them in the plan's Decisions with ids continuing from the spec, and writes plan `status: draft`. (D14, D16)
- [ ] AC7: Given a plan not marked `status: approved`, when `/tasks` runs, then it stops and asks for approval. (D6)
- [ ] AC8: Given `/tasks`, when it writes tasks, then each task names the `AC` ids it covers.
- [ ] AC9: Given a git repo, when `/implement` finishes a task with tests passing, then it commits as `<spec id>: <task number> <summary>`; it also commits on spec or plan approval; it never pushes. (D12)
- [ ] AC10: Given no git repo, when `/implement` runs, then it skips commits, says so once, and does not create a repo. (D18)
- [ ] AC11: Given a grill, when a term is settled or a word clashes with the glossary, then the glossary is updated at once or the clash is raised. (D17)
- [ ] AC12: Given a decision, when an ADR is offered, then only if it is hard to reverse, surprising, and a real trade-off. (D17)
- [ ] AC13: Given the glossary or decisions folder is missing, when a grill needs it, then the user is asked first; yes creates it with the real entry and adds a row to the root agent file; no keeps the item in Decisions and stops asking for that spec. (D17)
- [ ] AC14: Given a new project, when scaffolded, then the glossary uses bold term, short definition, `_Avoid_:` synonyms, and the ADR guide uses the short format (title, Status, Date, 1-3 sentences, optional sections). (D8, D9)
- [ ] AC15: Given adapted grilling text, when shipped, then each adapted skill ends with a one-line credit and its folder holds the full license text. (D10)
- [ ] AC16: Given specs 001-004 and ADRs 0001-0002, when this ships, then they are unchanged. (D19)

## Out of scope

- Reverse specs and adopting SDD on existing code.
- A skill for the friction log.
- A quick or one-round grill mode (D5).

## Decisions

Settled while grilling. Newest last.

- D1: Scope is (a) Decisions section in spec, (b) plan status, (c) acceptance criterion ids, (d) `/implement` commits, (e) 3-part ADR test in `/plan`, (f) round-based grilling in `/spec`. Reverse specs and a friction-log skill are out (own specs later).
- D2: Grilling is adapted into our own skill text with credit, not called from an outside plugin. Works for users without that plugin.
- D3: Keep our doc locations for glossary and decisions.
- D4: Change both the shipped templates and this repo's own process files.
- D5: No quick mode. Grilling stops when no decision is open; the user can say "enough" and the rest goes to Open questions.
- D6: Plan approval lives in the plan's own front matter: `status: draft | approved`. Tasks are refused until the plan is approved.
- D7: Acceptance criteria get ids `AC1`, `AC2`... Renumber freely while the spec is draft; frozen once approved. A dropped criterion stays, struck out, marked dropped; its id is never reused.
- D8: Glossary switches to bold term + short definition + `_Avoid_:` synonyms, in shipped and repo copies.
- D9: ADR format becomes short: title, Status, Date, 1-3 sentences, optional sections. Existing ADRs are not rewritten.
- D10: Credit for adapted text: one line at the bottom of each adapted skill, full license text in a separate file in the same skill folder.
- D11: `/spec` creates the spec first and writes each decision here the moment it is settled.
- D12: `/implement` commits once per task after tests pass, message `<spec id>: <task number> <summary>`. It also commits when a spec or plan is approved. It never pushes.
- D13: No ADR for D2; it is easy to undo, so it fails the "hard to reverse" test.
- D14: `/plan` also grills, so design choices reach the user before the plan is written. Widens D1.
- D15: Decisions get ids `D1`, `D2`...; same freeze rule as acceptance criteria (D7).
- D16: `plan.md` gets its own Decisions section; ids continue from the spec's last decision, so ids are unique per spec folder.
- D17: While grilling, `/spec` and `/plan` write settled terms to the glossary at once, flag words that clash with it, and offer an ADR only when a decision is hard to reverse, surprising, and a real trade-off. If the glossary or decisions folder is missing, ask before creating it; on yes, create it with the real entry and add a row to the root agent file; on no, keep the item in the spec's Decisions and do not ask again for that spec.
- D18: If the project is not a git repo, `/implement` skips commits and says so once. It never creates a repo.
- D19: Specs 001-004 keep their old format; the new format applies from 005 on.

## Open questions

- None.
