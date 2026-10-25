# Week 3 — Local state ≠ live orders

## Problem

Your bot’s JSON says there is a stop. The exchange does not. Or the exchange has a stop your local file forgot after a restart. Either way, “I thought I was protected” is how small accounts get wrecked.

Local protect rules are **intent**.  
Live open orders are **truth**.

## Failure modes

1. **Wrote SL to disk, never placed** — crash between write and API call.
2. **Placed SL, local file overwritten** — restart loads stale intent; watchdog is green on heartbeat while the book is naked.
3. **Partial fills / replace** — local TP/SL ids drift from exchange ids.

## Shape that works

1. **Reconcile before arming** — on boot and on a timer, pull open orders; compare to local intent; alert on mismatch.
2. **Schema without secrets** — public/sanitized `protect.json` holds prices and caps only. Keys stay in a private env the doctor never prints.
3. **`require_live_reconcile: true`** — if a config claims “local only is enough”, fail the check.

## Minimal check (public)

```bash
PYTHONPATH=. python3 -m agent_ops check-config --root samples/ok
# rejects secret-like keys; requires require_live_reconcile=true
```

Also folded into `doctor` when `protect.json` is present.

## What I publish vs keep private

| Public | Private |
|--------|---------|
| Schema, reconcile rule, failure stories | API keys, real symbols/sizes, account ids |
| Sample `protect.json` with EXAMPLE | Live stop placement path |

## Next

Week 4: a short “how I use agent-ops in a week” strangers can follow in two minutes.
