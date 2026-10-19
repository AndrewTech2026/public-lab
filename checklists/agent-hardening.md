# Agent hardening checklist

Use before an autonomous agent can place orders, send messages, or change production state.

## Must have

- [ ] Kill switch / `armed=false` (or env flag) that blocks all side effects
- [ ] Hard stop on max loss / consecutive failures (time-bounded cooldown)
- [ ] Stops and limits verified on the **exchange/API**, not only in local state
- [ ] Secrets only in env / secret store — never in git
- [ ] Cron / scheduler inventory: one owner script, no ghost jobs

## Nice to have

- [ ] Dry-run mode that prints intended actions without executing
- [ ] Alert on "process up but no heartbeat"
- [ ] After any forced flatten: cooldown before re-entry

## Anti-patterns seen in the wild

- Trusting local "SL is set" when the live order was cancelled
- Stop price beyond liquidation (stop never saves you)
- Multiple scripts fighting the same position
- All-in high leverage with no equity floor

This checklist is intentionally boring. Boring is how agents stay alive.
