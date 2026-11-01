# Research brief fixture

**Fake events in → short text brief out.** No exchange client, no keys, no orders.

This is the public half of “research ≠ execution” ([note](../../notes/research-vs-execution.md)). Live scanners stay private.

## Run

```bash
python3 brief.py
python3 brief.py --min-importance 0.5 --top 2
```

## Test

```bash
python3 test_brief.py
```

## Shape

| File | Role |
|------|------|
| `events.json` | Sample headlines with kind / importance / tags |
| `brief.py` | Rank, drop noise, print a short briefing |
| `test_brief.py` | Stdlib unit tests |

Importance threshold defaults to `0.3`; `kind=noise` is always dropped.
