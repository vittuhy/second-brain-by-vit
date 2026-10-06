---
title: Processed recordings
type: note
created: 2026-10-05
updated: 2026-10-05
tags: [voice, inbox, triage]
summary: Ledger of which recorded conversations have already been triaged and where their content went
---
# Processed recordings

The record of what has already gone through triage from `inbox/Conversations/` and where the content went. Belongs to [[voice-capture]].

**Why it exists:** a sync plugin keeps its own state outside the repository. After a reinstall, a new phone or a full re-scan it downloads old conversations again. This table is the only place that tells you they were already handled. Without it they would be processed twice.

**How a folder leaves the inbox:** `/triage` deletes it after the transcript is saved to `sources/transcripts/` and a row is written here.

**When a folder reappears** and is already in this table, it is a leftover from a full re-scan. Delete it, do not process it again.

---

| date | conversation | transcript | where the content went | deliberately left out |
|---|---|---|---|---|
