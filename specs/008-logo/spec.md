---
id: 008-logo
title: Logo
status: done
created: 2026-11-11
---

# Logo

## Problem

strata has no visual identity. The repo page is plain text, so it is hard to spot and remember next to other tools.
A logo makes the project recognizable on GitHub and anywhere it is linked.

## User stories

- As a developer browsing GitHub, I want to see a clear logo at the top of the repo so that I recognize strata at a glance.
- As a developer using GitHub in dark mode, I want the logo to stay legible so that it does not vanish on a dark background.
- As the maintainer, I want the logo files in the repo under the project license so that anyone can reuse them without asking.

## Acceptance criteria

- [x] AC1: Given the repo, when I look for the logo, then I find four versions: mark alone, mark with name for light grounds, mark with name for dark grounds, and a small icon. (D1, D3)
- [x] AC2: Given any version, when I compare it with the chosen concept, then shapes and colors match D1. (D1)
- [x] AC3: Given the README on GitHub in light theme, when the page loads, then the light-ground lockup shows at the top; in dark theme, the dark-ground lockup shows. (D3, D4)
- [x] AC4: Given the README, when read by a screen reader or a search engine, then the logo has text alternative "strata" and the page title is still plain text. (D4)
- [x] AC5: Given a machine without the Space Grotesk font, when a lockup is viewed, then the name looks the same as on a machine that has it. (D5)
- [x] AC6: Given the small icon shown at 16 pixels, when viewed, then the three plates are still distinct. (D6)
- [x] AC7: Given a project made by `strata init`, when I list its files, then no logo file is present. (D2)
- [x] AC8: Given the license, when I read it, then it covers the logo files with the rest of the repo. (D7)

## Out of scope

- Logo inside projects that `strata init` creates.
- GitHub social preview card, docs site, stickers, other merch.
- A brand or trademark guide.

## Decisions

Settled while grilling. Newest last.

- D1: Mark is concept C "Plates": three stacked isometric plates. Top plate accent orange #E8743B, middle #6B7385, bottom #14171F. On dark ground: middle #8C95A6, bottom #F2F3F5. Wordmark "strata", lowercase, Space Grotesk 600. Chosen from 4 concepts on the design canvas https://claude.ai/artifact/61WQHTcVt67ZAFFbxRaG2X.
- D2: Logo is this repo's own branding only (README, GitHub page). Not shipped in scaffolds.
- D3: Four versions: mark alone, lockup (mark + name) for light grounds, lockup for dark grounds, small icon.
- D4: README shows the lockup at the top, switching with the viewer's light or dark theme. The page title stays as text below it, for accessibility and search.
- D5: The name in the lockups is drawn as shapes, so it renders the same without the font installed.
- D6: The small icon is the same three-plate mark, not simplified; it holds at 16 pixels.
- D7: Logo files are covered by the project's MIT license. No separate brand terms.

## Open questions

- None.
