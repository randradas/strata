# Conventions

## Code

- Python 3.12+, type hints, `from __future__ import annotations`.
- `cli.py` handles I/O only; logic lives in `scaffold.py` (or new modules beside it).
- Errors from logic are exceptions; the CLI turns them into a message on stderr and exit code 1.

## Tests

- Every task in `tasks.md` ships with tests that prove its acceptance criteria.
- Test through `sdd_init.cli.main([...])` with `tmp_path`; avoid mocking the filesystem.
- Run: `uv run pytest`.

## Git

- One spec per branch: `spec/NNN-slug`.
- Commit message references the spec id, e.g. `004-profiles: add profile flag`.
