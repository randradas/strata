---
id: 004-profiles
title: Profiles
status: approved
created: 2026-11-11
---

# Profiles

## Problem

`sdd init` always writes the full scaffold (15 files). Small projects and side scripts do not need
a glossary, ADRs or four skills. Unfilled docs stay full of TODOs, which adds noise for people and
gives agents context with nothing in it. Users need to pick how much structure they start with.

## User stories

- As a developer on a small project, I want a minimal scaffold so that I only get files I will fill.
- As a developer on a larger project, I want the full scaffold so that every layer exists from day one.
- As a user, I want to see which profiles exist and what each one adds so that I can choose well.

## Acceptance criteria

- [ ] Given no profile chosen, when I run `sdd init`, then I get the same full scaffold as today (no change for current users).
- [ ] Given I choose the `minimal` profile, when I run `sdd init`, then I get only: the root agent file, product doc, specs workflow guide with spec templates, and all four workflow skills (spec, plan, tasks, implement).
- [ ] Given the `minimal` profile, when a skill tells the agent to read a doc that was not created, then the skill says to skip it, not fail.
- [ ] Given the `minimal` profile, when I read the root agent file, then it does not point to docs or skills that were not created.
- [ ] Given I choose the `full` profile, when I run `sdd init`, then the result is the same as choosing no profile.
- [ ] Given an interactive terminal and no profile flag, when I run `sdd init`, then I am asked to pick a profile, defaulting to `full`.
- [ ] Given an unknown profile name, when I run `sdd init`, then nothing is written, valid names are listed, and exit code is 1.
- [ ] Given I ask for the profile list, when the command runs, then each profile is shown with a one-line description.
- [ ] Given a `minimal` project, when I run `sdd spec new`, then it works the same as in a full project.
- [ ] Given any profile, when `sdd init` finishes, then the chosen profile is recorded in the project in a place a later command can read.

## Out of scope

- Upgrading an existing project from one profile to another (the recorded profile makes this possible later).
- A `team` profile. Add when we know what it needs.
- User-defined profiles outside the tool.
- Profiles for agents other than Claude Code.

## Decisions

- Two profiles in v1: `minimal` and `full`.
- `minimal` trims docs, not workflow: all four skills stay.
- The chosen profile is recorded in the project.

## Open questions

- None.
