# Tasks: Profiles

Order matters. Each task: small, testable, maps to an acceptance criterion.

Acceptance criteria (numbered in `spec.md` order):
AC1 no profile = full, unchanged · AC2 minimal file set · AC3 skills skip missing docs ·
AC4 minimal `CLAUDE.md` has no dangling links · AC5 `full` = no profile · AC6 interactive prompt, default full ·
AC7 unknown profile: nothing written, names listed, exit 1 · AC8 profile list · AC9 `spec new` in minimal ·
AC10 profile recorded

- [x] T1: Write failing tests for AC1-AC10, plus a guard that only `CLAUDE.md` overlaps between layers. (all)
- [ ] T2: Split `templates/project/` into `templates/base/` + `templates/full/` (git mv). Add `profiles.py` with `full` only; `init_project` merges layers. v0.1 tests stay green. (AC1, AC5)
- [ ] T3: Add `templates/minimal/CLAUDE.md`, register `minimal`, add `--profile` with registry validation (exit 1, list names). (AC2, AC4, AC7, AC9)
- [ ] T4: Add `base/dot-sdd.toml` with `profile` and `sdd_version`; pass both as render vars. (AC10)
- [ ] T5: Interactive profile prompt, default `full`. (AC6)
- [ ] T6: `sdd profiles` command. (AC8)
- [ ] T7: Plan and implement skills: optional docs read "if it exists". (AC3)
- [ ] T8: Repo process + docs: this repo's `.sdd.toml` (`profile = "full"`), `docs/architecture.md`, `README.md`.
- [ ] T9: Full `uv run pytest`, tick every AC in `spec.md`, set `status: done`.
