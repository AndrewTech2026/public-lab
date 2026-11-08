# Pre-launch ops: honest metrics, invite gate, public incidents

Shipped **2026-11-08** (cadence target was 2026-11-07).

## Problem

Right before a real user wave, dashboards lie in three boring ways:

1. **Empty cohorts show `0%`.** Looks like “everyone failed,” actually means “nobody finished the funnel yet.”
2. **Shared rate limits.** One noisy client trips a global bucket; unrelated users get blocked.
3. **Incidents stay internal.** Trust dies when outsiders only hear rumors.

## What I shipped in private this week (sanitized pattern)

| Piece | Rule I want in public notes |
|-------|------------------------------|
| Daily ops metrics | If sample size is too small → label **「no data yet」**, never invent a rate |
| Monthly AI / infra cost | Split by feature + per-active-user; schedule on the 1st |
| Invite-only registration | Feature flag **off by default**; wrong / exhausted / expired codes get clear copy |
| Incident transparency | Public page + RSS; no login required for the status board |
| Rate limit | **Per principal** (user / API key), not one global hammer |

None of that is glamorous. All of it is what you want *before* marketing turns the faucet on.

## Tiny load check (order-of-magnitude only)

- Users arriving **staggered**: most first paints stayed snappy.
- Users arriving in the **same second**: latency spiked — queued as a follow-up (queueing / shed load / cache), not a vanity merge.

Numbers stay private; the lesson is: test both arrival shapes, not only the happy ramp.

## What I’d do next

- Keep the invite flag dark until support can mint and revoke codes offline.
- Alert when a metric flips from「no data」to a real rate — that transition is the first honest signal.
- Treat the transparency page as part of the product, not a blog afterthought.

## Anti-goal

Green-square commits with no private improvement behind them. This note exists because the pre-launch ops work actually landed.
