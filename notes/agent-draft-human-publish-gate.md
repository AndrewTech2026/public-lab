# Agent drafts content; humans publish

Shipped **2026-11-14** (twice-weekly cadence; slot was due 11-11).

## Problem

It’s easy to let an agent “finish” a quiz / questionnaire end-to-end: write items, score keys, and ship. That speed is real — and it’s how you publish a bad bank on a Friday night.

What goes wrong:

1. **Draft and release share one mutable file.** Yesterday’s live version disappears; you can’t diff “what users saw.”
2. **Import APIs that also publish.** One token leak or one over-eager agent run goes straight to production.
3. **Validation after publish.** Schema errors show up as user-facing blank results instead of a blocked review.

## What I tried this week

A content shape that keeps agents useful without giving them the ship button (generic; no product names):

| Layer | Who writes | Rule |
|-------|------------|------|
| Draft JSON | Human form **or** agent import | Mutable; revision / concurrency check on replace |
| Validate | API | Duplicate IDs, missing refs, score ranges, unreachable results |
| In review | Agent may *submit* | Still not live |
| Release `vN.json` | Human only | Immutable; new version = new file; auto local git commit as audit trail |

Agent kit rules that mattered:

- Generate against a **JSON Schema + one close example**, not vibes.
- Call import → validate → **submit for review**. Never call publish.
- On replace, send `expectedRevision`. Blind overwrite races are silent corruption.

## What I’d do next

- Keep OpenAPI + schema in the same repo as the drafts so the agent kit can’t drift from the server.
- Treat “publish creates a git commit” as the audit log; push to remote stays a human step.
- For viral quiz packs, same gate: factory output is a pack on disk; H5/prod only after a human click.

## Anti-goal

Farming green squares. This note exists because the draft→review→immutable release path was the thing under the microscope this week — not because the calendar said “post something.”
