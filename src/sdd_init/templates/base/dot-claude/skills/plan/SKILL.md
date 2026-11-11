---
name: plan
description: Turn an approved spec into a technical plan. Use when a spec is approved and the user wants a design, or says /plan.
---

# Write a plan

1. Find the spec (argument or newest in `specs/`). Stop if `status` is not `approved`.
2. Read `docs/architecture.md` and `docs/conventions.md`, each only if it exists. Read code only where the plan touches it.
3. Fill `plan.md`: approach, changes table, risks, test strategy.
4. If a choice is lasting, draft an ADR in `docs/decisions/` if it exists; otherwise record it under "Approach" in `plan.md`.
5. Ask the user to approve the plan.
