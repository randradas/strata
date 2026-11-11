---
id: 006-rename
title: Rename
status: draft
created: 2026-11-11
---

# Rename

## Problem

The tool is called `sdd` / `sdd-init`. The command name is taken on PyPI, so package and command can
never match. "init" undersells a tool that also creates, lists and (later) checks specs. And `sdd`
is easy to swap with "ssd". The name should say what the tool is about: layered context.

## User stories

- As a user, I want one memorable name for the tool, its command and its package so that I can find, install and type it without thinking.
- As a reader of the docs, I want the method (SDD) and the tool (strata) kept apart so that I am never unsure which one is meant.

## Acceptance criteria

- [ ] AC1: Given the tool is installed, when I run `strata`, then every current command works (`init`, `spec new`, `spec list`, `profiles`) and help and version say `strata`. (D1)
- [ ] AC2: Given the tool is installed, when I run `sdd`, then there is no such command. (D2)
- [ ] AC3: Given the package, when built, then its name is `strata-sdd`, version 0.4.0, and its description is the tagline. (D1, D6, D8, D9)
- [ ] AC4: Given a new project, when scaffolded, then every file and message names `strata`, never `sdd` as the tool; "SDD" appears only as the method. (D3, D5)
- [ ] AC5: Given a new project, when scaffolded, then its config file is named after `strata` and records profile and version as before. (D3)
- [ ] AC6: Given this repo, when the spec is done, then its own process files, docs, glossary and README use `strata`, and the glossary defines SDD and strata. (D3, D4, D5)
- [ ] AC7: Given this repo, when the spec is merged, then the user gets exact commands to rename the folder and reinstall. (D7)
- [ ] AC8: Given specs 001-005 and ADRs 0001-0002, when this ships, then they are unchanged; they keep the old name as history.

## Out of scope

- Publishing to PyPI.
- A migration command for projects made with `sdd`.
- An alias for the old `sdd` command (D2).

## Decisions

Settled while grilling. Newest last.

- D1: The tool is named `strata`: command `strata`, package `strata-sdd` (bare `strata` is taken on PyPI).
- D2: The old `sdd` command is dropped, no alias. Nobody outside this repo uses it.
- D3: The name is used everywhere: command, package, Python module, config file, template text, CLI messages, docs, and this repo's folder.
- D4: Only this repo is migrated. No migration command for other old projects.
- D5: "SDD" stays as the name of the method (spec driven development); `strata` is the tool. Both are glossary terms.
- D6: The Python module is `strata_sdd`, matching the package, so it cannot clash with the other `strata` package. Users only type `strata`.
- D7: The repo folder is renamed last, after the merge, by the user, with commands given by the agent; then the tool is reinstalled from the new folder.
- D8: Tagline: "strata: layered specs and context for AI coding agents."
- D9: Version 0.4.0, a minor bump, because the old command breaks.

## Open questions

- None.
