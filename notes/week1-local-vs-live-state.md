# Week 1 — Never trust local state alone

## Problem

An agent wrote “stop-loss is set” into a local JSON file. On the exchange, that trigger had been cancelled. The next cron cycle skipped re-placing the stop because **local state still matched**. The position ran naked until price moved enough to force a refresh — or until liquidation.

## What I tried

- Treat local state as a cache, not as truth.
- Before skipping a protect order, **query live open orders** (the API that actually returns trigger fields).
- If live SL is missing, place it again even when the cache says “already done”.

## Rule I keep

```text
if protect_required and not live_protect_visible:
    place_or_flatten()
# never: if cache_says_ok: skip
```

## What I'd do next

- Same pattern for take-profit and for “armed” flags: env/file can claim armed; a doctor command should prove the process that matters is the one cron calls.
- Encode the check in [`agent-ops`](https://github.com/AndrewTech2026/agent-ops) so it’s boring and repeatable.

## Links

- Checklist: [`../checklists/agent-hardening.md`](../checklists/agent-hardening.md)
