---
name: spec
description: Draft a new feature spec (what and why, no how). Use when the user wants to start a feature, write a spec, or says /spec.
---

# Write a spec

1. Read `specs/README.md` and `docs/product.md`. Read other docs only if needed.
2. Create the spec first: run `strata spec new "<title>"`. If `strata` is missing, copy `specs/_template/` to the next `specs/NNN-slug/`.
3. Run the `grill` skill on the feature. Decisions land in the spec's `## Decisions` as they are settled.
4. When the grill ends, write Problem, User stories and Acceptance criteria (`AC1`, `AC2`...; each names the decisions it comes from).
5. Keep it tech free. No file names, no libraries.
6. Leave `status: draft`. Ask the user to approve. On approval set `status: approved` and commit (rules: `specs/README.md`, Commits).
