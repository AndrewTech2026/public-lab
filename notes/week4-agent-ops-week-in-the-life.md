# Week 4 — How I use agent-ops in a week

Strangers should be able to clone, run the sample doctor, and understand the weekly rhythm — not my private trading stack.

## The one reliability win (sanitized)

Across weeks 1–3 the same lesson kept showing up in different clothes:

**Green squares on a process list are not safety.**

| Week | Symptom that looked “fine” | What actually mattered |
|------|----------------------------|------------------------|
| 1 | Kill switch in a config file | The scheduler still called a different script |
| 2 | `ps` showed the agent | Heartbeat file was frozen |
| 3 | Local JSON had a stop | Exchange book did not |

`agent-ops` exists so the first question is always: **doctor the export**, then argue about strategy.

## A normal week (public shape)

Daily (or on a launchd interval — see `samples/watchdog/`):

```bash
python3 samples/refresh_heartbeat.py   # only for the sample fixture
PYTHONPATH=. python3 -m agent_ops doctor --root /path/to/sanitized-ops-export
```

Exit `0` → ok to keep side effects armed.  
Exit `≠ 0` → fix crons / heartbeat / armed / protect schema before anything that can spend money or send DMs.

When I change protect intent (stops, caps):

```bash
PYTHONPATH=. python3 -m agent_ops check-config --root /path/to/sanitized-ops-export
```

No API keys in that file. `require_live_reconcile` stays `true`.

## Two-minute proof (no accounts needed)

```bash
git clone https://github.com/AndrewTech2026/agent-ops.git
cd agent-ops
python3 samples/refresh_heartbeat.py
PYTHONPATH=. python3 -m agent_ops doctor --root samples/ok    # exit 0
PYTHONPATH=. python3 -m agent_ops doctor --root samples/bad   # exit 1
PYTHONPATH=. python3 -m agent_ops check-config --root samples/ok
```

## What stays private

Live roots, exchange clients, real symbols/sizes, alert channel wiring.  
Public repos get the checklist and the fixtures.

## After this 4-week arc

Cadence slows to ~twice a week. Next public slice (calendar): a tiny **research fixture** — fake events in, brief text out — still no exchange client.
