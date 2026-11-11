# Glossary

One line per term. Use these words in code, specs, and talk.

| Term | Meaning |
|---|---|
| Spec | What and why of a feature. No how. |
| Plan | How we will build a spec. |
| Task | Small, testable step from a plan. |
| Shipped template | File under `src/sdd_init/templates/` (layers); what users get. |
| Repo process files | This repo's own `CLAUDE.md`, `docs/`, `specs/`, `.claude/`. |
| Target project | Directory `sdd` writes into. |
| Progressive disclosure | Root doc is a short map; detail sits one link away and loads on demand. |
| Reverse spec | Spec written after the fact to record existing behaviour (`status: done`). |
| Grill | Round-based interview that settles every open decision of a spec or plan before writing it. |
| Decision | A settled choice in a spec or plan, with an id (`D1`...) unique within its spec folder. |
| Acceptance criterion | One testable Given/When/Then line of a spec, with an id (`AC1`...). |
