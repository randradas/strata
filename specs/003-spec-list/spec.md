---
id: 003-spec-list
title: Spec list
status: done
created: 2026-11-11
---

# Spec list

Reverse spec: records v0.1 behaviour.

## Problem

With many specs, it is hard to see at a glance what exists and where each one stands.

## User stories

- As a developer, I want to list specs with their status so that I know what to work on next.

## Acceptance criteria

- [x] Given specs exist, when I run `sdd spec list`, then each `NNN-slug` is shown with the `status` from its `spec.md` front matter, in number order.
- [x] Given a spec without a readable status, when listed, then its status shows as `unknown`.
- [x] Given no specs, when I run `sdd spec list`, then I see `No specs yet.`
- [x] Given `specs/_template/` and `specs/README.md`, when listing, then they are not shown as specs.

## Out of scope

- Filtering by status, JSON output.

## Open questions

- None.
