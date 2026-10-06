---
title: Tasks
type: context
created: 2026-10-05
updated: 2026-10-05
tags: [tasks, triage]
summary: "The one running checklist of concrete actions, written short so it can be read from a home screen widget"
---
## Now

- [ ] Run /setup to finish onboarding

## Soon

## Waiting for a date

## Done

---

## How this works

One list of concrete things to do. `/triage` fills it, you tick it off by hand, nothing notifies you.

**It can be read from a home screen widget** (Obsidian widget, "View a note"), and that decides the format:

- **No text above the first task.** The widget draws the note from the top, so even an H1 heading is one invisible task. That is why the file starts straight with the Now section and this explanation sits at the bottom.
- **One line per task.** A long sentence wraps to three lines and eats the space of two other tasks. Detail belongs in a note, here only what is needed to recognise the task.
- **No wikilinks and no emoji.** The widget does not render them. Context can be found in the vault, the list does not need to carry it.
- **A short date in brackets at the end**, like `(Oct 10)`. Nothing rings, it is only ordering. A task without a deadline has no date.

**What this is not.** [[now]] describes **state**, this file holds **actions**. "The supplier has not replied since March" is state. "Call the supplier" is an action. Never write the same thing to both.

**Housekeeping.** Move ticked items to Done, `/weekly` empties Done. Above about ten items in Now the list stops being read and `/weekly` says so.

**If you prefer the Tasks or TaskForge plugin**, they expect `📅 2026-10-10`. That is a find and replace, not a rewrite.
