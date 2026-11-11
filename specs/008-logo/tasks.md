# Tasks: Logo

Order matters. Each task: small, testable, names the acceptance criteria it covers.

- [x] T1: Failing tests: new `tests/test_logo.py` for files, SVG validity, D1 colors, no `<text>`/font refs, README `<picture>` + alt + heading, no `.svg` from `strata init`, no extra license in `assets/`. (AC1, AC2, AC3, AC4, AC5, AC7, AC8)
- [x] T2: `assets/logo/strata-mark.svg` and `strata-icon.svg`: three plates, D1 colors, inline dark-mode switch (D10); icon tight-cropped. (AC1, AC2, AC6)
- [x] T3: Outline "strata" in Space Grotesk 600 with a throwaway `uvx` fonttools script in the scratchpad; keep the path data only (D11). (AC5)
- [x] T4: `assets/logo/strata-lockup-on-light.svg` and `strata-lockup-on-dark.svg`: mark + outlined wordmark, ground colors per D1. (AC1, AC2, AC5)
- [x] T5: README: `<picture>` block with theme sources and `<img alt="strata">` above `# strata` (D12). (AC3, AC4)
- [ ] T6: Checks: `uv run pytest` green; render icon at 16 px and lockups next to the design canvas, by eye; tick ACs, spec `status: done`. (AC2, AC6, AC8)
