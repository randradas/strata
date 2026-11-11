---
status: approved
---

# Plan: Workflow fixes

Spec: `spec.md` (approved). Decision ids continue from the spec (D16).

## Approach

Text changes, almost no code: `sdd spec new` already copies whatever the templates say.

1. **New `grill` skill** (D20). It merges the round-based interview with domain modelling, adapted from
   Matt Pocock's `grilling` + `domain-modeling` (MIT). It names our paths (`docs/glossary.md`,
   `docs/decisions/`) and the ask-before-create rule for missing files (D17). It must stay
   model-invocable, so `/spec` and `/plan` can call it. Target: under ~60 lines.
2. **Rewire the four skills.** `/spec`: create first, run `grill`, ids. `/plan`: refuse unless spec approved,
   run `grill` on design choices, decisions continue ids, write `status: draft`, three-part ADR test.
   `/tasks`: refuse unless plan approved, every task names its AC ids. `/implement`: commits per the rules, no-git fallback.
3. **Templates.** Spec: `AC1:` format + Decisions. Plan: `status: draft` front matter + Decisions.
   Tasks: `- [ ] T1: ... (AC1)`. `specs/README.md`: plan status in lifecycle, id freeze rule, Commits section (D22).
   Glossary: bold term + `_Avoid_:`. ADR guide: short format.
4. **Repo copies** (D4, D21). Copy every shared file into this repo, then add the drift test so they stay equal.
   Convert this repo's glossary by hand (its content is ours, not the template's).
5. Bump to 0.3.0.

## Decisions

Settled while grilling the plan. Newest last.

- D20: The grill method lives in a new `grill` skill (adapted text, credit, license in one folder). `/spec` and `/plan` run it; users can also run `/grill` alone. Every project gets 5 skills.
- D21: A test fails if this repo's copies differ from the shipped ones for: skills, spec templates, `specs/README.md`, ADR guide. Glossary and root agent file are excluded (content differs by design). First sync the repo's `plan` and `implement` skills to the shipped versions.
- D22: Commit rules live once, in a "Commits" section of `specs/README.md`. `/spec`, `/plan` and `/implement` each carry one line pointing there.
- D23: Done = automated content tests pass, plus one smoke run: scaffold a throwaway project, run `/spec` on a toy feature with headless Claude, show the transcript to the user. Real behaviour is checked again when 006 is grilled.

## Changes

| Area / file | Change |
|---|---|
| `templates/base/dot-claude/skills/grill/SKILL.md` | New: adapted grill method + domain modelling + credit line. |
| `templates/base/dot-claude/skills/grill/LICENSE-mattpocock-skills.md` | New: full MIT text, Matt Pocock copyright. |
| `templates/base/dot-claude/skills/{spec,plan,tasks,implement}/SKILL.md` | Rewire as in Approach step 2. |
| `templates/base/specs/_template/{spec,plan,tasks}.md` | New formats (step 3). |
| `templates/base/specs/README.md` | Lifecycle with plan status, id freeze rule, Commits section. |
| `templates/full/docs/glossary.md` | Bold term + `_Avoid_:` format. |
| `templates/full/docs/decisions/README.md` | Short ADR format. |
| `.claude/skills/**`, `specs/_template/**`, `specs/README.md`, `docs/decisions/README.md` (repo) | Copied from shipped versions. |
| `docs/glossary.md` (repo) | Converted to new format; `_Avoid_` words proposed below. |
| `tests/test_profiles.py` | File sets gain the two `grill` files. |
| `tests/test_workflow.py` | New: content checks per AC + drift test. |
| `src/sdd_init/__init__.py`, `pyproject.toml` | 0.3.0. |

Proposed `_Avoid_` words for this repo's glossary (change freely at approval):
Spec: PRD, story, ticket · Plan: design doc, RFC · Task: step, todo · Grill: interview, Q&A ·
Decision: choice, answer · Acceptance criterion: requirement, check · Shipped template: scaffold file ·
Target project: output dir.

## Risks and mitigations

- **Claude does not call `grill` from `/spec`.** Skill text names it explicitly; the description says when to use it; smoke run (D23) checks it.
- **Name clash with other grill skills** (e.g. Matt's `grilling`, `grill-me`). Our name `grill` is distinct; project skills win in their folder.
- **Skills grow and eat context.** `grill` stays short; skills point to `specs/README.md` instead of repeating rules.
- **Repo copy edited, shipped copy forgotten (or reverse).** Drift test (D21).
- **Content tests are weak proof.** Accepted (D23); smoke run + 006 dogfood cover behaviour.

## Test strategy

| AC | Check |
|---|---|
| AC1-AC3 | `grill` skill: rounds, numbered, recommended answer, "yes" accepts, facts looked up, write decision at once, stop on empty or "enough" -> Open questions. `spec` skill: creates first, runs `grill`. Smoke run. |
| AC4 | Spec template has `AC1:` and `## Decisions`. |
| AC5 | `specs/README.md` states freeze rule (draft renumber, frozen when approved, struck out, never reused). |
| AC6 | `plan` skill runs `grill`, ids continue, writes `status: draft`; plan template has front matter + Decisions. |
| AC7 | `tasks` skill refuses unless plan `status: approved`. |
| AC8 | `tasks` skill + template require AC ids per task. |
| AC9 | README Commits section: message format, approval commits, never push; skills point to it. |
| AC10 | `implement` skill: no git -> skip, say once, never `git init`. |
| AC11-AC13 | `grill` skill: glossary at once, clash raised, three-part ADR test, ask before creating, add root-file row, stop asking for that spec. |
| AC14 | Generated `full` project: glossary has `_Avoid_:`; ADR guide short format. |
| AC15 | `grill` folder has license file; skill ends with credit line. |
| AC16 | `git diff main -- specs/00[1-4]-* docs/decisions/000[12]-*` is empty at the end. |
| Drift | Shared files byte-equal between shipped and repo copies. |
