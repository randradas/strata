# Smoke run (D23)

Throwaway `minimal` project, git repo, headless `claude -p "/spec Tag notes and filter by tag"`, 2026-11-11.
Reply style is caveman because the user's global agent config asks for it, not because of the skills.

## Output

> Spec made: `specs/001-tag-notes-and-filter-by-tag/`. Repo has no code yet. Now grill time. Round 1.
> 
> **Q1. Tag shape.** One word only. Letters, digits, hyphen. No spaces. Case not matter: `Work` = `work`. Yes?
> 
> **Q2. Many tags.** Note can have zero, one, or many tags. Same tag twice on one note does nothing. Yes?
> 
> **Q3. When to tag.** User can tag at create time. User can also add and remove tags later. Yes?
> 
> **Q4. Tags show in note.** Tags show inside the note text. User can edit them by hand, and hand edits count. Yes?
> 
> **Q5. Filter.** User can filter by one or more tags. Note must have *all* of them (AND, not OR). Yes?
> 
> **Q6. Tag list.** User can list all tags, with a count of notes for each. Yes?
> 
> **Q7. No match.** Filter finds nothing: show "no notes" message. Not an error. Yes?
> 
> **Q8. Glossary.** No `docs/glossary.md` yet. Make it now and add the word **tag**? Yes?
> 
> Answer by number. "yes all" works too.

## Seen

- AC1: spec created before grilling; round of numbered questions, each with a recommended answer, "yes" accepts; facts looked up ("no code yet").
- AC13: missing glossary, asked before creating (Q8).
- Not reachable headless: rounds 2+, writing decisions, approval commits. Checked again when 006 is grilled.
