---
name: grill
description: Interview the user in rounds until every decision of a spec or plan is settled, recording decisions, glossary terms and ADRs as they land. Use from /spec and /plan, or when the user wants an idea stress-tested.
---

# Grill

Reach shared understanding. Nothing silently assumed.

## Rounds

1. Map the open decisions as a tree: each decision unlocks the ones that hang off it.
2. The **frontier** is every decision whose prerequisites are settled. Ask the whole frontier in one round.
3. Number each question (continue numbering across rounds). Give your recommended answer, and word the question so "yes" accepts it.
4. Facts are your job: look up code, files and docs yourself (use a sub-agent for big searches). Only decisions go to the user.
5. Wait for answers. Recompute the frontier. Next round.

## Write as you go

- Write each settled decision at once to the `## Decisions` section of the spec or plan you are grilling, with the next `D` id (ids are unique per spec folder; a plan continues from its spec).
- Stop when the frontier is empty or the user says "enough". Anything still open goes to `## Open questions`.

## Language

- When a term is settled, add it at once to `docs/glossary.md`: bold term, one-line meaning, `_Avoid_:` synonyms. No implementation details.
- When the user's words clash with the glossary, or one word means two things, raise the clash and pick one term.

## ADRs

Offer an ADR in `docs/decisions/` only when the decision is all three: hard to reverse, surprising to a future reader, and the result of a real trade-off. Otherwise the `D` entry is enough.

## Missing files

If `docs/glossary.md` or `docs/decisions/` does not exist, ask the user before creating it.
- Yes: create it with the real entry, and add a row for it to the "Where to look" table in `CLAUDE.md`.
- No: keep the item in `## Decisions` and do not ask again for this spec.

Adapted from Matt Pocock's `grilling` and `domain-modeling` skills (MIT, see LICENSE-mattpocock-skills.md).
