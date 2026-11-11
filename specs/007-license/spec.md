---
id: 007-license
title: License
status: in-progress
created: 2026-11-11
---

# License

## Problem

strata has no license. Without one, nobody may legally use, copy or change it, so the tool cannot
be shared. There is a second problem: `strata init` copies shipped templates into the user's repo.
A plain license could be read as making users carry strata's notice in their own `CLAUDE.md` and
docs. Nobody wants that, and it would put people off.

## User stories

- As a developer, I want to know strata's license at a glance so that I can tell whether I may use it.
- As a user of `strata init`, I want the files it writes to be mine, with no notice to keep, so that my repo stays clean.
- As a user, I want to pick my own project's license so that strata never decides it for me.

## Acceptance criteria

- [ ] AC1: Given the repo, when I look at its root, then I find the standard MIT license text, unchanged, with the line "Copyright (c) 2026 Roberto Andradas Izquierdo". (D1, D5, D6)
- [ ] AC2: Given the repo, when I look next to the license, then a short statement says files strata writes into a target project belong to the user and need no strata notice. (D2, D6)
- [ ] AC3: Given that statement, when I read it, then it says text adapted from others keeps its own license and notice, and it names the grill skill. (D4)
- [ ] AC4: Given the built package, when I read its metadata, then it says MIT and includes the license text and the statement. (D1, D2, D8)
- [ ] AC5: Given the built package, when I read its version, then it is 0.4.1. (D8)
- [ ] AC6: Given the README, when I read it, then a License section names MIT, gives the D2 promise and notes the third-party text. (D7)
- [ ] AC7: Given a new project, when scaffolded, then it gets no strata license or notice file, and the grill skill still ships with its own license file. (D2, D3, D4)

## Out of scope

- Picking or writing a license for target projects (D3).
- Adding license headers to source files.
- Publishing to PyPI.

## Decisions

Settled while grilling. Newest last.

- D1: strata is released under the MIT license.
- D2: Files `strata` writes into a target project belong to the user. They need no strata copyright or license notice.
- D3: strata does not pick or write a license for target projects. That is the user's call.
- D4: Exception to D2: text adapted from others keeps its own license and notice. Today that is only the grill skill, which already ships its license file.
- D5: Copyright line: "Copyright (c) 2026 Roberto Andradas Izquierdo".
- D6: The license text stays standard MIT, word for word, so tools detect it. The D2 promise is a separate short statement next to it.
- D7: The README gets a License section: MIT, the D2 promise, the third-party note.
- D8: Version 0.4.1, a patch bump, because the package metadata changes.

## Open questions

- None.
