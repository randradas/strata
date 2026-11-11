# Product: sdd-init

CLI (`sdd`) that scaffolds projects for spec driven development with progressive disclosure docs, tuned for Claude Code.

## Problem

AI coding agents work best with clear intent and focused context. Most repos give them neither:
one giant instructions file (wastes context, goes stale) or nothing at all (agent guesses intent).
Setting up a spec workflow and a layered doc structure by hand takes time, and every project does it differently.

## Users

- Developers starting a new project with Claude Code who want a repeatable spec -> plan -> tasks -> code loop.
- Teams that want one shared, predictable layout across repos.

## Goals

- One command gives a working SDD skeleton: short `CLAUDE.md`, layered `docs/`, `specs/` with templates, Claude Code skills.
- Progressive disclosure by default: root file is a map; detail loads only when a task needs it.
- Day-to-day helpers for specs (create, list) so the workflow stays low-friction.
- Zero runtime dependencies; installs anywhere `uv` or `pip` runs.

## Non-goals

- Not a project generator for code (no app frameworks, no language boilerplate).
- Not a task tracker or a replacement for issues/PRs.
- Not an agent runtime; it writes files that agents read.

## Success measures

- `sdd init` on an empty dir produces a skeleton Claude Code can follow with no extra setup.
- This repo is developed using `sdd` itself without workarounds.
