# Research agent stays read-only

## Problem

A single agent that both "looks around" and "places orders" will eventually mix the two. A research brief, a chat reply, or a stale cron becomes an accidental trade. The failure mode is not a bad idea — it is one process holding both jobs.

## What I tried

Split them:

| Process | May do | Must not do |
|---------|--------|-------------|
| Research | Read public markets, write a brief, stay silent when nothing changed | Import an exchange client, flip an `armed` flag, place or cancel orders |
| Execution | One owner cron, its own config, its own kill switch | Treat a research note as an order |

Concrete shape:

1. Config `mode` must be `readonly`. Anything else exits before network calls that matter.
2. The research entrypoint does not import the trading client.
3. Stdout is the brief. Empty stdout means "no change" — the scheduler does not nag.
4. A fingerprint plus a minimum interval stops the same story from posting every few minutes.
5. The brief text says it is not an instruction. The execution cron never reads that file to trade.

## Rule I keep

```text
research_process  = read + report
execution_process = one script, armed default false
shared_state      = none that can place an order
```

## What I'd do next

- Add a tiny public fixture (fake events in, brief out) so this rule is testable without API keys.
- Keep the live scanner, wallets, and chat delivery off GitHub.

## Links

- Checklist: [`../checklists/agent-hardening.md`](../checklists/agent-hardening.md)
- Doctor CLI: [agent-ops](https://github.com/AndrewTech2026/agent-ops)
