---
name: spec
description: Draft a new feature spec (what and why, no how). Use when the user wants to start a feature, write a spec, or says /spec.
---

# Write a spec

1. Read `specs/README.md` and `docs/product.md`. Read other docs only if needed.
2. Run `sdd spec new "<title>"`. If `sdd` is missing, copy `specs/_template/` to the next `specs/NNN-slug/`.
3. Fill `spec.md` with the user. Ask questions; put unknowns in "Open questions".
4. Keep it tech free. No file names, no libraries.
5. Leave `status: draft`. Ask the user to approve.
