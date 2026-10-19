# Week 1 — A kill switch that actually blocks

## Problem

“Manual mode” in one config file doesn’t help if cron still calls a different script, or an env flag is `1` in the shell that launches the job. I ended up with overlapping jobs: one paused on paper, another still live.

## Shape that works

1. **One owner entrypoint** — cron/launchd calls exactly one script for trading (or agent side effects).
2. **Armed defaults false** — missing flag = no orders / no outbound side effects.
3. **Doctor before blame** — when something fires, first question is “which binary did the scheduler run?”, not “why did the strategy lose”.

## Minimal pattern

```json
{ "armed": false, "comment": "flip true only when doctor is green" }
```

```bash
# scheduler → wrapper → python
# wrapper refuses to exec if armed is false or env KILL=1
```

## What I publish vs keep private

| Public | Private |
|--------|---------|
| Patterns, sample configs, CLI checks | Live keys, coin lists, real equity |
| Failure stories without addresses | Exchange account details |

## Next

Week 2 notes will cover heartbeats: **PID running ≠ job healthy**.
