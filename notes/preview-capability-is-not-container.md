# Preview capability is not container capability

Shipped **2026-11-25** (twice-weekly cadence).

## Problem

An offline mini-tool got a “listen / speak” control that worked fine in the local browser preview: `speechSynthesis`, English voices, kid-friendly rate. Shipping felt one click away.

The host container tells a different story:

- no official TTS / speech API in the platform surface
- no outbound network for cloud TTS
- packaged `<audio>` may be described in docs, while the upload validator’s extension allowlist still rejects common audio types
- Chinese-device WebViews often expose only `zh-*` voices, so English gets mangled when synthesis “works”

If you leave the button on, first-time users in the real container get silence, a Chinese voice chewing English, or a control that looks broken. That’s worse than no feature.

## What I tried this week

Treat preview success as **non-evidence** for container shipping:

| Check | Rule |
|-------|------|
| Platform API list | If TTS isn’t listed, don’t sell “pronunciation” |
| Runtime detect | Prefer host SDK presence (`miniTool`-style) over “API exists in Chrome” |
| Soft degrade | Hide the speak control in-container; keep it for local demos only |
| Packaging | Don’t bet the release on media types the validator won’t accept |
| Copy | Parent-led read-aloud beats a fake speaker icon |

Same class of bug as “works on my laptop” CI: the wrong environment greenlights the wrong promise.

## What I’d do next

- Any Web API used in an offline / sandboxed host: maintain a **three-column table** — browser preview, container docs, upload validator — and ship only the intersection.
- QA gate: open the packaged build inside the real simulator/device path before marketing a capability.
- If audio becomes allowed later, pack short clips and play with `<audio>`; don’t resurrect system TTS as the product story.

## Anti-goal

Farming green squares. This note exists because a pronunciation control almost shipped on preview confidence alone — and got gated before the awkward release.
