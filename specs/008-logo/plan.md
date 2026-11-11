---
status: approved
---

# Plan: Logo

Spec: `spec.md` (must be `approved` before this is filled). Decision ids continue from the spec.

## Approach

Repo branding only; no shipped template or package change (D2, AC7 gets a test).
Draw the Plates mark (D1) as hand-written SVG on a 64x64 grid, as on the design canvas.
Outline the "strata" wordmark once from Space Grotesk 600 with a throwaway script; commit only the
resulting SVG paths. Put four files in `assets/logo/`, show the lockup at the top of `README.md`
with a `<picture>` theme switch, and guard it all with `tests/test_logo.py`.

## Decisions

Settled while grilling the plan. Newest last.

- D8: Logo files live in `assets/logo/` at the repo root, outside `src/`, so the package never ships them.
- D9: File names: `strata-mark.svg`, `strata-lockup-on-light.svg`, `strata-lockup-on-dark.svg`, `strata-icon.svg`.
- D10: Mark and icon carry their own dark-mode colors via an inline `prefers-color-scheme` style, so one file works on both grounds. Lockups stay fixed, one per ground (D3).
- D11: Wordmark outlined once by a throwaway script (font tools run via `uvx`, outside the project). Script and font file are not committed; zero runtime and dev dependencies added. Space Grotesk is OFL, which allows outlined glyphs in a logo.
- D12: README uses `<picture>` with `prefers-color-scheme` sources, `<img alt="strata">` fallback, relative paths. `# strata` heading stays below it. Absolute URLs deferred until PyPI publish.
- D13: Tests in a new `tests/test_logo.py` (files, SVG validity, D1 colors, no `<text>`, README block, no logo from `strata init`). AC6 checked once by eye in the last task.
- D14: Version stays 0.4.1; nothing in the package changes.

## Changes

| Area / file | Change |
|---|---|
| `assets/logo/strata-mark.svg` | New: three plates, D1 colors, dark-mode switch (D10). |
| `assets/logo/strata-icon.svg` | New: same mark, tight crop for 16-32 px, dark-mode switch (D6, D10). |
| `assets/logo/strata-lockup-on-light.svg` | New: mark + outlined wordmark, light-ground colors (D1, D5). |
| `assets/logo/strata-lockup-on-dark.svg` | New: mark + outlined wordmark, dark-ground colors (D1, D5). |
| `README.md` | `<picture>` block above `# strata` (D12). |
| `tests/test_logo.py` | New tests (D13). |

## Risks and mitigations

- Font outlining needs the font file and a tool not in the project: run once via `uvx --from fonttools`, in the scratchpad; if unavailable, stop and ask.
- Some favicon hosts ignore media queries in SVG: icon then shows light colors, still legible on light tab bars. Accepted.
- PyPI will not render relative README images: noted in D12, fix with the PyPI publish spec.
- Wordmark metrics drift from the canvas: compare side by side with the design canvas in the last task.

## Test strategy

| AC | Check |
|---|---|
| AC1 | `test_logo.py`: all four files exist in `assets/logo/` and parse as SVG. |
| AC2 | `test_logo.py`: each file uses the D1 colors for its ground; manual compare with the canvas. |
| AC3 | `test_logo.py`: README has `<picture>` with light and dark `prefers-color-scheme` sources pointing at the lockups. |
| AC4 | `test_logo.py`: `<img alt="strata">` present and `# strata` heading still in README. |
| AC5 | `test_logo.py`: lockups contain no `<text>` element and no font reference. |
| AC6 | Manual: render the icon at 16 px, three plates distinct. |
| AC7 | `test_logo.py`: `strata init` into `tmp_path` writes no `.svg` file. |
| AC8 | `test_logo.py`: `LICENSE` is MIT and logo files sit in the repo outside any other license's scope (no separate license file in `assets/`). |
