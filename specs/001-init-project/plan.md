# Plan: Init project

Reverse spec: built in v0.1 before the SDD process existed.

## Approach

See `docs/architecture.md` (Data flow, Template rules).

## Changes

| Area / file | Change |
|---|---|
| `src/sdd_init/` | scaffold.init_project, cli.cmd_init |

## Test strategy

- `tests/test_cli.py` covers the acceptance criteria.
