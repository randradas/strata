---
id: 002-spec-new
title: Spec new
status: done
created: 2026-11-11
---

# Spec new

Reverse spec: records v0.1 behaviour.

## Problem

Creating a spec folder by hand (pick next number, copy three templates, fill ids) is tedious and error prone.

## User stories

- As a developer, I want to create a numbered spec from a title so that every feature starts the same way.
- As a team, I want spec templates to live in the project so that we can tailor them.

## Acceptance criteria

- [x] Given an initialised project, when I run `sdd spec new "User Login!"`, then `specs/NNN-user-login/` holds `spec.md`, `plan.md`, `tasks.md`.
- [x] Given existing specs, when I create a new one, then its number is the highest existing number + 1, zero padded to 3.
- [x] Given the new files, when I open them, then id, title and date are filled and no `{{...}}` remains.
- [x] Given I edited `specs/_template/`, when I create a spec, then my edited templates are used.
- [x] Given no `specs/_template/`, when I run `sdd spec new`, then I get an error telling me to run `sdd init`, exit code 1.

## Out of scope

- Changing spec status from the CLI.

## Open questions

- None.
