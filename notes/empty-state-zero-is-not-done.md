# Empty states that lie: zero activity is not “all done”

Shipped **2026-11-21** (twice-weekly cadence; slot was due 2026-11-18).

## Problem

A “today’s review” card is supposed to pull people back. The first version did the opposite for new users.

Logic was roughly: count words that are due to review. If the count is `0`, show **“all mastered for today.”**

What “due” meant after a safety fix:

- only count words the learner had **already practiced**
- so a brand-new account → due = 0 → celebration UI

New users opened the tool and got a gold-star empty state before they’d done anything. Trust dies quietly: the product looks finished when it’s actually idle.

## What I tried this week

Split the empty state into **three** states, not two:

| State | Meaning | UI |
|-------|---------|-----|
| Has due items | Practiced words that need another pass | “N words to review · ~M min” + start |
| Practiced, nothing due | Real “caught up” | Soft done, no fake fireworks |
| Never practiced | Cold start | “Nothing to review yet — pick a pack below” + scroll/CTA |

Rules that mattered:

1. **Zero rows is ambiguous.** It can mean “caught up” or “never started.” Don’t celebrate until you’ve seen at least one practice signal (`lastAt` / equivalent).
2. **Retention hooks must not lie.** A review entry that fires before first use trains people to ignore it.
3. **Cold start needs a next action.** “You’re done” with nowhere to go is worse than a quieter prompt that points at the catalog.

Same class of bug as dashboard charts that show “100% healthy” because the metrics pipeline never ingested data.

## What I’d do next

- Any “streak / mastered / inbox zero” surface: require a **positive evidence gate** before the win state.
- Add a one-line analytics check in QA: first open with empty storage must not render the celebration copy.
- Keep the review card, but treat cold start as onboarding, not retention.

## Anti-goal

Farming green squares. This note exists because a real empty-state bug shipped and got fixed in an offline mini-tool this week — not because the calendar was empty.
