# public-lab — 4-week content calendar

Goal: fill the GitHub story so a stranger can tell what I'm drilling into.
Parallel track (private): keep hardening the real agent stack every week; publish only the sanitized lesson here.

| Week | Theme | Ship in `public-lab` | Ship in `agent-ops` | Private agent work (not published raw) |
|------|--------|----------------------|---------------------|----------------------------------------|
| **1** (this week) | Failure modes & kill switches | 2 notes + this calendar | v0.1 CLI: `doctor`, `crons`, `heartbeat`, `armed` | Audit live crons; confirm one owner script; armed flag respected |
| **2** | Heartbeats & watchdogs | 1 note: “process up ≠ healthy” | `heartbeat` age thresholds + sample launchd/plist snippet (generic) | Wire watchdog alerts; fix false positives |
| **3** | Stops & exchange truth | 1 note: local state vs live orders | `check-config` for JSON schema of protect rules (no exchange keys) | SL/TP path regression on paper or tiny size |
| **4** | One demo strangers can run | Short “how I use agent-ops in a week” | Release tag `v0.1.0` + GIF or asciinema in README | Pick one reliability win; write the public summary |

## Weekly ritual (after week 4, keep forever)

1. **Private:** one concrete agent improvement (bugfix, test, or ops alert).
2. **Public:** one commit in `public-lab` or `agent-ops` that captures the lesson (no secrets).
3. **Profile:** leave pins as-is unless a new public repo clearly deserves a slot.

## Anti-goals

- Fake green-square commits
- Open-sourcing live trading configs or keys
- Building a paid landing page before the public story is solid

## Done when (end of week 4)

- [ ] Calendar weeks 1–4 each have a matching public commit
- [ ] `agent-ops` README: install → run `doctor` on the included sample fixtures in &lt; 2 minutes
- [ ] Profile pins include `public-lab` + `agent-ops` (drop profile-repo pin if you only want 2 product signals)
