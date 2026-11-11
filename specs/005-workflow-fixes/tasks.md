# Tasks: Workflow fixes

Order matters. Each task names the acceptance criteria it covers.

- [x] T1: Failing tests: content checks per AC, `grill` files in profile file sets, drift test. (AC1-AC15)
- [x] T2: `grill` skill + license file. (AC1, AC2, AC3, AC11, AC12, AC13, AC15)
- [ ] T3: Spec template (`AC1:` ids, Decisions) + `/spec` skill (create first, run grill). (AC1, AC4)
- [ ] T4: Plan template (status, Decisions) + `/plan` skill (refuse unapproved spec, grill, ids continue, ADR test). (AC6, AC12)
- [ ] T5: Tasks template + `/tasks` skill (refuse unapproved plan, AC ids per task). (AC7, AC8)
- [ ] T6: `specs/README.md` (lifecycle, freeze rule, Commits) + `/implement` skill (commits, no-git). (AC5, AC9, AC10)
- [ ] T7: Shipped glossary (`_Avoid_`) + ADR guide (short format). (AC14)
- [ ] T8: Copy shared files into this repo, convert repo glossary; drift test green. (D4, D21)
- [ ] T9: Bump 0.3.0, check old specs/ADRs untouched, smoke run, tick ACs, `status: done`. (AC16, D23)
