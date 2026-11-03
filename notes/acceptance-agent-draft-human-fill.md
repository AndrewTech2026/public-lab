# Acceptance docs: agent draft, human fill

Shipped **2026-11-04** (twice-a-week cadence after the early fill).

## Problem

An agent can walk a product happy path and stamp PASS / FAIL with screenshots. That is useful — and incomplete.

What usually goes wrong:

1. **SKIP / PARTIAL stay empty** unless a human runs the awkward paths (register flows, dual-subject accounts, ops-only cron demos).
2. **The overview table goes stale.** Agent writes “mock exam SKIP”; human later finishes that path; nobody rewrites the summary. Stakeholders read the wrong verdict.
3. **“Needs eng / DB” items get mixed into product FAIL.** Staging-only checks look like production bugs if you don’t bucket them.

## What I tried this week

A two-layer acceptance doc (generic shape; no product secrets):

| Layer | Owner | Contents |
|-------|--------|----------|
| Case + evidence | Agent first | Steps, PASS/FAIL/PARTIAL/SKIP, short evidence |
| Your result | Human | Checkboxes under every SKIP/PARTIAL; free-text when UI lies |
| Stakeholder table | Human after pass | One row per ID: over / fail / untested / needs eng |

Rules that saved time:

- **Overview is not SSOT** after hand-fill starts. Either regenerate it or delete it before you paste to eng.
- **Star the soft passes.** Main path green + attached content bug → `PASS*` and a separate ticket, not a silent green.
- **Bucket “needs eng”** (clear old consent rows, cron sweeps, DB flags) so the human night doesn’t block on staging access.

## What I’d do next

- Keep a one-page “fill order” (~1–2 hours) so the human pass isn’t random.
- When agent and human disagree (same journey different account), write the account/session on the FAIL row — otherwise eng thinks the doc contradicts itself.

## Anti-goal

Farming green squares with empty commits. This note exists because the acceptance pass actually happened; the lesson is the process, not the product under test.
