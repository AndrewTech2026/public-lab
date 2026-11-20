# public-lab — 4-week content calendar

Goal: fill the GitHub story so a stranger can tell what I'm drilling into.
Parallel track (private): keep hardening the real agent stack every week; publish only the sanitized lesson here.

| Week | Theme | Ship in `public-lab` | Ship in `agent-ops` | Private agent work (not published raw) |
|------|--------|----------------------|---------------------|----------------------------------------|
| **1** (this week) | Failure modes & kill switches | 2 notes + this calendar | v0.1 CLI: `doctor`, `crons`, `heartbeat`, `armed` | Audit live crons; confirm one owner script; armed flag respected |
| **2** | Heartbeats & watchdogs | 1 note: “process up ≠ healthy” | `heartbeat` age thresholds + sample launchd/plist snippet (generic) | Wire watchdog alerts; fix false positives |
| **3** | Stops & exchange truth | 1 note: local state vs live orders | `check-config` for JSON schema of protect rules (no exchange keys) | SL/TP path regression on paper or tiny size |
| **4** | One demo strangers can run | Short “how I use agent-ops in a week” | Release tag `v0.1.0` + GIF or asciinema in README | Pick one reliability win; write the public summary |

## Shipped outside the weekly theme

- **2026-10-20** — [`notes/research-vs-execution.md`](notes/research-vs-execution.md): a research process does not share an order path with the execution process. Live scanner stays private. Next public steps are every ~3 days through **2026-10-31** (see [`NEXT.md`](NEXT.md)).
- **2026-10-23** — [`notes/week2-process-up-not-healthy.md`](notes/week2-process-up-not-healthy.md) + `agent-ops` v0.1.1 (warn/hard heartbeat ages, launchd sample).
- **2026-10-25** — [`notes/week3-local-state-vs-live-orders.md`](notes/week3-local-state-vs-live-orders.md) + `agent-ops` v0.1.2 (`check-config`).
- **2026-10-28** — [`notes/week4-agent-ops-week-in-the-life.md`](notes/week4-agent-ops-week-in-the-life.md) + agent-ops README demo refresh.
- **2026-11-01** — [`samples/research-brief/`](samples/research-brief/) + [`notes/research-brief-fixture.md`](notes/research-brief-fixture.md) (fake events → brief; no exchange client).
- **2026-11-04** — [`notes/acceptance-agent-draft-human-fill.md`](notes/acceptance-agent-draft-human-fill.md) (agent draft + human fill; overview is not SSOT).
- **2026-11-08** — [`notes/prelaunch-ops-honest-metrics.md`](notes/prelaunch-ops-honest-metrics.md) (honest metrics, invite gate, public incident page).
- **2026-11-14** — [`notes/agent-draft-human-publish-gate.md`](notes/agent-draft-human-publish-gate.md) (agent drafts; human publishes; immutable `vN`).
- **2026-11-21** — [`notes/empty-state-zero-is-not-done.md`](notes/empty-state-zero-is-not-done.md) (zero activity ≠ “all mastered”).

## Cadence

- **Now through 2026-10-31:** one real public commit about every 3 days. Dates are in [`NEXT.md`](NEXT.md).
- **After that:** twice a week. Still one private improvement and one sanitized lesson. No empty green-square commits.

## Anti-goals

- Fake green-square commits
- Open-sourcing live trading configs or keys
- Building a paid landing page before the public story is solid

## Done when (end of week 4)

- [x] Week 1 public commits landed (calendar + 2 notes)
- [x] Week 2 public commit landed (process up ≠ healthy + agent-ops v0.1.1)
- [x] Week 3 public commit landed (local state vs live orders + agent-ops v0.1.2)
- [x] Week 4 public commit landed (agent-ops week-in-the-life + README demo refresh)
- [x] `agent-ops` README: install → run `doctor` on the included sample fixtures in &lt; 2 minutes
- [x] Profile pins include `public-lab` + `agent-ops` (+ profile README)
