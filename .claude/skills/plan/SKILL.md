---
name: plan
description: Turn an approved spec into a technical plan. Use when a spec is approved and the user wants a design, or says /plan.
---

# Write a plan

1. Find the spec (argument or newest in `specs/`). Stop if its `status` is not `approved`.
2. Read `docs/architecture.md` and `docs/conventions.md`, each only if it exists. Read code only where the plan touches it.
3. Create `plan.md` with `status: draft` first.
4. Run the `grill` skill on the design choices. Decision ids continue from the spec's last `D` id.
5. Fill the rest: approach, changes table, risks, test strategy (one row per `AC`).
6. Offer an ADR only if a choice is hard to reverse, surprising, and a real trade-off (the `grill` skill says where).
7. Ask the user to approve. On approval set `status: approved` and commit (rules: `specs/README.md`, Commits).
