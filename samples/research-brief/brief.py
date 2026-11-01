#!/usr/bin/env python3
"""Fake events → short research brief. No exchange client. Stdlib only."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def load_events(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or "events" not in data:
        raise ValueError("events.json must be an object with an `events` list")
    if not isinstance(data["events"], list):
        raise ValueError("`events` must be a list")
    return data



def event_importance(e: dict) -> float:
    raw = e.get("importance", e.get("significance", 0))
    try:
        return float(raw or 0)
    except (TypeError, ValueError):
        return 0.0

def rank(events: list[dict]) -> list[dict]:
    def score(e: dict) -> float:
        if e.get("kind") == "noise":
            return -1.0
        return event_importance(e)

    return sorted(events, key=score, reverse=True)


def render(data: dict, *, min_importance: float = 0.3, top_n: int = 3) -> str:
    as_of = data.get("as_of") or "unknown"
    ranked = [
        e
        for e in rank(data["events"])
        if event_importance(e) >= min_importance and e.get("kind") != "noise"
    ][:top_n]

    lines = [
        f"Research brief (fixture) — as of {as_of}",
        "Scope: sanitized sample events only. No orders. No exchange API.",
        "",
        "Top signals:",
    ]
    if not ranked:
        lines.append("- (none above threshold)")
    else:
        for i, e in enumerate(ranked, 1):
            tags = ",".join(e.get("tags") or [])
            lines.append(
                f"{i}. [{e.get('kind', '?')}] {e.get('headline', '(no headline)')}"
                f"  (importance={event_importance(e)}; tags={tags})"
            )
    lines.append("")
    lines.append("Not advice. Research process must not share an order path with execution.")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Render a short brief from fake research events.")
    p.add_argument(
        "--events",
        type=Path,
        default=Path(__file__).resolve().parent / "events.json",
        help="Path to events.json",
    )
    p.add_argument("--min-importance", type=float, default=0.3)
    p.add_argument("--top", type=int, default=3)
    args = p.parse_args(argv)

    try:
        data = load_events(args.events)
        sys.stdout.write(render(data, min_importance=args.min_importance, top_n=args.top))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
