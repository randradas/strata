---
status: approved
---

# Plan: Question marker

Spec: `spec.md` (must be `approved` before this is filled). Decision ids continue from the spec.

## Approach

Shipped template change plus the matching repo copy (D2). Rewrite step 3 of the grill skill's
`## Rounds` to require the `◈` marker before each question number and to keep it off everything
else. Same text in both copies; the existing sync test (005 D21) guards drift. Bump to 0.4.2.

## Decisions

Settled while grilling the plan. Newest last.

- D5: Grill `## Rounds` step 3 becomes: "Start each question with the question marker `◈`, then its number (continue numbering across rounds), e.g. `◈ 7. Folder. ... Yes?`. Only questions get the marker." The rest of step 3 (recommended answer, "yes" accepts) stays.
- D6: Tests go in `tests/test_workflow.py` beside the grill tests: marker and `◈ 7.` format named, "only questions" rule present. Sync between copies stays with the existing 005 D21 test.
- D7: Version 0.4.2 in `pyproject.toml` and `__init__.py`; pins in `test_name.py` and `test_license.py` move with it.

## Changes

| Area / file | Change |
|---|---|
| `src/strata_sdd/templates/base/dot-claude/skills/grill/SKILL.md` | Step 3 per D5. |
| `.claude/skills/grill/SKILL.md` | Same text (D2). |
| `tests/test_workflow.py` | New marker tests (D6). |
| `pyproject.toml`, `src/strata_sdd/__init__.py` | 0.4.2 (D7). |
| `tests/test_name.py`, `tests/test_license.py` | Version pins 0.4.2 (D7). |

## Risks and mitigations

- Projects made before 0.4.2 keep the old grill: no upgrade command exists. Accepted; noted in the commit.
- The agent may still drop the marker sometimes: the rule names it and shows an example, which is the strongest lever a skill text has.
- Non-UTF-8 terminals may show `◈` badly: rare today; accepted.

## Test strategy

| AC | Check |
|---|---|
| AC1 | `test_workflow.py`: shipped grill names `◈` and the `◈ 7.` example. |
| AC2 | `test_workflow.py`: shipped grill says only questions get the marker. |
| AC3 | `test_workflow.py` runs against a project made by `strata init`, so the marker rule is what users get. |
| AC4 | Existing 005 D21 sync test: repo grill equals shipped grill. |
| AC5 | `test_workflow.py` or manual: `docs/glossary.md` has **Question marker** (done in spec approval commit). |
