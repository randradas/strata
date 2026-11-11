# Plan: Spec new

Reverse spec: built in v0.1 before the SDD process existed.

## Approach

See `docs/architecture.md` (Data flow, Template rules).

## Changes

| Area / file | Change |
|---|---|
| `src/sdd_init/` | scaffold.new_spec, scaffold.next_spec_number, scaffold.slugify |

## Test strategy

- `tests/test_cli.py` covers the acceptance criteria.
