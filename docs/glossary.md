# Glossary

Project words only. One or two lines each. Use these words in code, specs, and talk.
Format: **Term**: what it is. `_Avoid_:` words that mean the same thing but should not be used.

## Workflow

**Spec**:
What a feature must do and why. No how.
_Avoid_: PRD, story, ticket

**Plan**:
How a spec will be built.
_Avoid_: design doc, RFC

**Task**:
A small, testable step of a plan.
_Avoid_: step, todo

**Grill**:
Round-based interview that settles every open decision of a spec or plan before writing it.
_Avoid_: interview, Q&A

**Decision**:
A settled choice in a spec or plan, with an id (`D1`...) unique within its spec folder.
_Avoid_: choice, answer

**Acceptance criterion**:
One testable Given/When/Then line of a spec, with an id (`AC1`...).
_Avoid_: requirement, check

**Reverse spec**:
Spec written after the fact to record existing behaviour (`status: done`).

## This tool

**Shipped template**:
File under `src/sdd_init/templates/` (layers); what users get.
_Avoid_: scaffold file

**Repo process files**:
This repo's own `CLAUDE.md`, `docs/`, `specs/`, `.claude/`.

**Target project**:
Directory `sdd` writes into.
_Avoid_: output dir

**Progressive disclosure**:
Root doc is a short map; detail sits one link away and loads on demand.
