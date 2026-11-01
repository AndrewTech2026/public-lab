# Research fixture — fake events → brief text

Shipped **2026-11-01** (calendar target was 2026-10-31).

## What

A tiny, runnable sample under [`samples/research-brief/`](../samples/research-brief/):

- Input: sanitized `events.json` (macro / crypto / noise)
- Output: a short briefing on stdout
- Tests: `python3 test_brief.py` (stdlib only)

## Why

Keeps the research path **demonstrable in public** without dragging in an exchange client. Execution and order placement stay private — same boundary as [research vs execution](research-vs-execution.md).

## Cadence after this

Early every-3-days fill is done. Next: ~twice a week, still one private improvement + one sanitized lesson.
