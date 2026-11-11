---
id: 009-question-marker
title: Question marker
status: in-progress
created: 2026-11-12
---

# Question marker

## Problem

Grill rounds are plain text. Questions sit among recommendations, context and recorded decisions,
so a user scanning a round can miss one or answer the wrong line.
A distinct marker tied to the strata look makes every question easy to spot.

## User stories

- As a user being grilled, I want each question to start with the same distinct symbol so that I spot every question at a glance.
- As a user being grilled, I want only questions marked so that the symbol always means "answer this".
- As a strata user, I want my generated projects to grill the same way this repo does so that the experience matches.

## Acceptance criteria

- [ ] AC1: Given a grill round, when questions are listed, then each one starts with `◈`, then its number, then the question. (D1, D3)
- [ ] AC2: Given a grill round, when it shows recommendations, settled decisions or other text, then none of it starts with `◈`. (D4)
- [ ] AC3: Given a project made by `strata init`, when its grill skill runs, then it uses the marker as in AC1 and AC2. (D2)
- [ ] AC4: Given this repo, when its own grill skill runs, then it uses the marker as in AC1 and AC2, and it matches the shipped grill skill. (D2)
- [ ] AC5: Given the glossary, when I look up the marker, then "Question marker" is defined. (D1)

## Out of scope

- Markers for other skills (spec, plan, tasks, implement).
- Color or styling beyond the plain symbol.
- Changing question numbering.

## Decisions

Settled while grilling. Newest last.

- D1: The question marker is `◈` (diamond in a diamond: echoes the stacked plates of the logo, spec 008).
- D2: Both grill copies change: the one shipped by `strata init` and this repo's own. They stay identical.
- D3: Format: marker, space, question number, then the question. Example: `◈ 7. Folder. Logo files go in assets/logo/. Yes?`
- D4: Only questions get the marker. Recommendations, recorded decisions and other text stay plain.

## Open questions

- None.
