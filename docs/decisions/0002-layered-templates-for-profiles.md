# 0002. Layered templates for profiles

Status: accepted
Date: 2026-11-11

## Context

Spec 004 adds `minimal` and `full` profiles. Profiles need different file sets, and the root
`CLAUDE.md` must not link to docs a profile does not create. Options:

1. One template tree + per-profile include lists, with conditional blocks inside `CLAUDE.md`.
2. Layered template dirs (`base` + one overlay per profile); later layers override same paths.
3. A full copy of the tree per profile.

## Decision

Option 2. A profile is an ordered list of layer dirs. Shared files live once in `base/`.
Profile-specific files (today only `CLAUDE.md`) live in the profile's layer.
The renderer stays plain `{{key}}` substitution with no conditionals.

The chosen profile is recorded in `.sdd.toml` in the target project. A missing file means `full`
(projects made before 0.2).

## Consequences

- Adding a profile = add a layer dir + one registry entry.
- Each profile's `CLAUDE.md` is maintained separately; a test checks its links resolve.
- Only `CLAUDE.md` may exist in more than one layer; a test enforces this to stop silent overrides.
