---
title: Voice capture
type: area
created: 2026-10-05
updated: 2026-10-05
tags: [vault, voice, capture]
summary: "How recordings from a voice assistant or recorder reach the inbox, how they are processed and what to watch for"
---
# Voice capture

Short version of [docs/voice-capture.md](../../docs/voice-capture.md), kept here so Claude can read it from inside the vault.

## The contract

Any recorder or assistant works if it leaves a folder in `inbox/Conversations/YYYY-MM-DD/<title>/` with a `transcript.md` (and optionally `summary.md` and `action-items.md`). The vault does not care which device made it. The reference setup is the Pocket AI recorder with the Pocket Sync plugin.

## Rules

- **The feed is not your file.** Never edit anything inside `inbox/Conversations/`, `inbox/Archive/` or `inbox/Insights/`. Read from it, write elsewhere.
- **Save the transcript before routing anything.** `sources/transcripts/YYYY-MM-DD-<slug>.md`, verbatim.
- **Delete the feed folder only after** the transcript is saved, the content is in the vault and a row is in [[processed-recordings]].
- **Summaries and action items are a model's guess.** The transcript is the truth. Dates and numbers from a summary are never copied without checking the transcript.

## Open items

