---
id: 001-init-project
title: Init project
status: done
created: 2026-11-11
---

# Init project

Reverse spec: records v0.1 behaviour.

## Problem

Setting up a spec workflow and layered docs by hand is slow and inconsistent between projects.

## User stories

- As a developer, I want one command to scaffold an SDD project so that I can start writing specs right away.
- As a developer, I want my existing files protected so that running the tool in a used folder is safe.

## Acceptance criteria

- [x] Given an empty dir, when I run `sdd init <dir>`, then `CLAUDE.md`, `docs/`, `specs/` (with `_template/`) and `.claude/skills/` are created.
- [x] Given an interactive terminal, when I run `sdd init` without flags, then I am asked for name, description and stack, with defaults.
- [x] Given `-y` or no terminal, when I run `sdd init`, then no prompts appear and defaults or flags are used.
- [x] Given project values, when files are written, then name, description and stack appear in `CLAUDE.md` and the docs.
- [x] Given any target file already exists, when I run `sdd init`, then nothing is written, the clashing files are listed, and exit code is 1.
- [x] Given `--force`, when files exist, then they are overwritten.
- [x] Given the scaffold, when I read `CLAUDE.md`, then it is a short map pointing to deeper docs, not a full manual.

## Out of scope

- Adding SDD to an existing codebase with generated architecture docs.
- Choosing a smaller or larger scaffold.

## Open questions

- None.
