---
name: tasks
description: Break an approved plan into ordered, testable tasks. Use after a plan is approved, or when the user says /tasks.
---

# Write tasks

1. Read the spec's `spec.md` and `plan.md`. If `plan.md` is not `status: approved`, stop and ask the user to approve it first.
2. Fill `tasks.md` with small steps (each under ~1 hour of work), format `- [ ] T1: <summary> (AC1, AC3)`.
3. Every task names the AC ids it covers, and every acceptance criterion is covered by at least one task.
4. Put tests first where you can.
