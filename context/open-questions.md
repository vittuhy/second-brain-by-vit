---
title: Open questions
type: context
created: 2026-10-05
updated: 2026-10-05
tags: [overview, open-question]
summary: Live list of every open question in the vault, built by an embedded search on the open-question tag
---
# Open questions

A live list. Nothing is copied here, it is pulled by a query, so it is always current.

```query
tag:#open-question -file:open-questions -file:CLAUDE
```

---

> **Note for the agent:** the block above is an embedded query that only Obsidian renders. From disk you read the query text, not the results. Always build the list of open questions by searching the vault for the tag `#open-question`, never by reading this file.

## What it is for

An open question is the third kind of content next to a fact and an action: **it is not decided, and I do not yet know what the action would be.** The rule is in CLAUDE.md. The marker is `#open-question` at the end of a bullet in the note where the topic belongs.

**An open question never goes to [[tasks]].** That file is for things you know how to do.

## How to get rid of one

Answer it and **delete the tag**, leave the answer standing in the note. It disappears from here and stays where it makes sense.

If the question turns into an action, it goes to [[tasks]] and the tag goes away too.

## Who asks you about them

`/weekly` harvests them but **does not show everything**: only questions in notes that moved since the last review, and those sitting for more than six weeks. A list of sixty would be skipped anyway.

## Fastest ways here

1. **Tap `#open-question`** anywhere in the text. It opens a search for the tag.
2. **Search** `tag:#open-question`.
3. **This file**, bookmarked. One tap from the sidebar.
