---
status: approved
---

# Plan: License

Spec: `spec.md` (must be `approved` before this is filled). Decision ids continue from the spec.

## Approach

Repo process change only; no shipped template changes (AC7 holds today and gets a test).
Add a plain MIT `LICENSE` and a separate `LICENSE-GENERATED.md` statement at the repo root.
Wire both, plus the shipped grill license, into the package metadata (PEP 639 fields, supported by
`uv_build`). Bump to 0.4.1. Add a README License section and ADR 0003.

## Decisions

Settled while grilling the plan. Newest last.

- D9: Work happens on branch `spec/007-license`; the approval commit moved there and `main` was reset to `375da16`.
- D10: Root files: `LICENSE` (standard MIT text) and `LICENSE-GENERATED.md` (the D2 statement), named like the existing `LICENSE-mattpocock-skills.md`.
- D11: Statement text, verbatim:

  ```
  # Files strata writes for you

  Files that `strata` writes into your project (`strata init`, `strata spec new`) are yours.
  Use, change, relicense or delete them. You need not keep strata's copyright or license notice.

  Exception: text adapted from others keeps its own license and notice. Today that is the
  `grill` skill (`.claude/skills/grill/`), which ships with `LICENSE-mattpocock-skills.md`.
  Keep that file with the skill.

  strata itself is MIT licensed, see `LICENSE`.
  ```

- D12: `pyproject.toml`: `license = "MIT"`; `license-files` = `LICENSE`, `LICENSE-GENERATED.md`, and the shipped grill license.
- D13: Tests in a new `tests/test_license.py`; `test_name.py` version pin moves to 0.4.1. Wheel metadata (AC4) is checked once by hand with `uv build` in the last task, so pytest stays fast.
- D14: ADR 0003 records the MIT choice and the generated-files promise, with rejected options: Apache-2.0, GPL, MIT-0 for templates, editing the MIT text.

## Changes

| Area / file | Change |
|---|---|
| `LICENSE` | New: standard MIT text, "Copyright (c) 2026 Roberto Andradas Izquierdo". |
| `LICENSE-GENERATED.md` | New: D11 text. |
| `pyproject.toml` | `version = "0.4.1"`, `license = "MIT"`, `license-files` (D12). |
| `src/strata_sdd/__init__.py` | `__version__ = "0.4.1"`. |
| `README.md` | New `## License` section: MIT, D2 promise, third-party note, links to both files. |
| `docs/decisions/0003-mit-license.md` | New ADR (D14). |
| `tests/test_license.py` | New: AC1-AC3, AC5-AC7 checks, AC4 pyproject fields. |
| `tests/test_name.py` | Version pin 0.4.0 -> 0.4.1. |

## Risks and mitigations

- `uv_build` 0.13 rejects or ignores `license-files` -> manual `uv build` in the last task; inspect `METADATA` for `License-Expression: MIT` and all three `License-File` entries.
- Hand-typed MIT text drifts from the standard -> test compares against the canonical SPDX MIT text.
- Version bump missed somewhere -> `test_name.py` already asserts pyproject and `__version__` agree.

## Test strategy

| AC | Check |
|---|---|
| AC1 | `LICENSE` equals the SPDX MIT text with the D5 copyright line. |
| AC2 | `LICENSE-GENERATED.md` exists and says generated files are the user's, no notice needed. |
| AC3 | Statement mentions adapted text keeps its own license and names the grill skill. |
| AC4 | pyproject `license == "MIT"` and `license-files` lists all three files, each existing; manual `uv build` METADATA check. |
| AC5 | pyproject version and `__version__` are `0.4.1`. |
| AC6 | README has `## License` naming MIT, the promise, the third-party note. |
| AC7 | `strata init` (each profile) writes no `LICENSE*` at the root; grill license still present. |
