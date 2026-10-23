# Week 2 — Process up ≠ healthy

## Problem

`ps` shows the agent. launchd says the job is loaded. You still get silent failure: no new heartbeat, no alert, and (worse) a false sense that “the bot is running.”

PID answers “is something alive?”  
Heartbeat age answers “is the loop still doing work?”

Those are different questions.

## Failure modes I hit

1. **Hung main loop** — process stays up; heartbeat file freezes.
2. **Wrong binary still scheduled** — watchdog watches PID A; cron runs script B.
3. **False “no heartbeat” pages** — threshold too tight vs write cadence → alert fatigue → people mute the pager.

## Shape that works

1. **Heartbeat is a write from the real work path** — not from a separate “I’m alive” shell that can outlive the worker.
2. **Two ages** — warn band, then hard fail. Soft warning first cuts false calm without paging on every jitter.
3. **Doctor exit code is the signal** — alert when `agent-ops doctor` ≠ 0. Do not alert on “PID missing” alone if the doctor already covers stale heartbeat + duplicate crons + armed.

## Minimal check

```bash
PYTHONPATH=. python3 -m agent_ops heartbeat --root /path/to/ops-export
# thresholds: config heartbeat_warn_age_s / heartbeat_max_age_s
# or CLI: --warn-heartbeat-age 120 --max-heartbeat-age 300
```

Generic macOS sample (edit paths, then load):

[`agent-ops/samples/watchdog`](https://github.com/AndrewTech2026/agent-ops/tree/main/samples/watchdog)

## What I publish vs keep private

| Public | Private |
|--------|---------|
| Threshold pattern, launchd template, CLI | Live alert channels, real ops paths, exchange clients |
| “PID listed but heartbeat stale” stories | Account IDs, keys |

## Next

Week 3: local protect-state vs live orders — doctor the JSON rules, never the keys.
