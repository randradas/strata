# Tasks: License

Order matters. Each task: small, testable, names the acceptance criteria it covers.

- [x] T1: Failing tests: new `tests/test_license.py` for every AC; `test_name.py` version pin 0.4.0 -> 0.4.1. (AC1, AC2, AC3, AC4, AC5, AC6, AC7)
- [x] T2: Add `LICENSE` (standard MIT, D5 copyright) and `LICENSE-GENERATED.md` (D11 text). (AC1, AC2, AC3)
- [x] T3: `pyproject.toml` gets `license` and `license-files` (D12); version 0.4.1 in `pyproject.toml` and `__init__.py`. (AC4, AC5)
- [ ] T4: README `## License` section: MIT, generated-files promise, third-party note, links. (AC6)
- [ ] T5: ADR `docs/decisions/0003-mit-license.md` (D14). (AC1, AC2)
- [ ] T6: Checks: `uv run pytest` green; `uv build` and confirm wheel METADATA has `License-Expression: MIT` and three `License-File` entries; tick ACs, spec `status: done`. (AC4, AC7)
