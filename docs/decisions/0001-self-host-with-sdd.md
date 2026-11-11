# 0001. Build sdd with sdd

Status: accepted
Date: 2026-11-11

## Context

`sdd` is a tool for spec driven development. v0.1 was written by hand before any spec existed.
We want the tool's own process to prove the workflow works.

## Decision

Bootstrap: run `sdd init .` on this repo, record v0.1 features as reverse specs (001-003, `status: done`),
and route all new work through `/spec` -> `/plan` -> `/tasks` -> `/implement`.

## Consequences

- Friction in the workflow shows up here first; fix it in the shipped templates.
- Two sets of similar files exist (shipped templates vs repo process files). `CLAUDE.md` states which is which.
