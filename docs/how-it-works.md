# How it works

## The idea

1. **Git is the canonical state, Markdown is the data.** Notes are Markdown files in a Git repository. Each vault on a disk is a working copy of it, and the latest pushed commit is the canonical shared state (with no remote, the folder is the only copy). Chat history is not storage; anything worth keeping is written to a file.
2. **Claude reads a few files before advising.** `about-me.md`, `goals.md`, `now.md`, and `decisions.md` for decisions. That is the whole "memory".
3. **Structure is cheap, consistency is everything.** Every note carries the same frontmatter, every folder answers one question, and a script checks it.
4. **Routines keep it alive.** The slash commands exist because systems rot when they rely on discipline.

## Three kinds of content

Everything you write is exactly one of these:

| Kind | Where | Example |
|---|---|---|
| **Fact** | A note | "The laptop warranty ends on 31 March, claims need a receipt." |
| **Action** | `context/tasks.md` | "Send warranty claim (Dec 15)" |
| **Open question** | A note, tagged `#open-question` | "Renew the subscription or cancel it? What would decide it? #open-question" |

Never write the same thing as an action and as a fact. The note carries the reasoning, the checklist carries the action.

## Folder routing

| Folder | Test |
|---|---|
| `inbox/` | Anything new. A queue, not a folder. To zero on Friday. |
| `context/` | What Claude must know before it advises you. |
| `collections/` | An item in a list you want to filter and sort. |
| `projects/` | A temporary outcome with a defined end: a decision, a deliverable or a change. |
| `areas/` | A lasting responsibility. The sentence "what should I do about this" exists. |
| `notes/` | A thought or finding with no responsibility and no list. |
| `sources/` | Verbatim sources (transcripts), not knowledge. Never edited. |
| `archive/` | No longer valid, not deleted. |
| `templates/` | Note templates. |
| `docs/` | These guides. |

Nothing lives in two folders at once.

### Project or area?

A **project** has an end: "choose a new laptop", "migrate the photo library", "launch the newsletter". When it is done, the outcome is recorded (a decision goes to `context/decisions.md`) and the folder moves to `archive/projects/`. An **area** does not end: finances, health, a relationship, a house. If you can imagine closing it, it is a project.

### Note, collection or area note?

If you want a table with filters (rating, status, cuisine), it is a collection. If it has a "what should I do about this" sentence, it is an area. If neither, it is a note.

## Frontmatter

Every note starts with:

```yaml
---
title: Choose a laptop
type: project          # note, context, project, area, source, book, film, place, recipe
created: 2026-10-05
updated: 2026-10-05    # set to today whenever the content changes
tags: [housing, finance]
summary: One English line saying what this note is. Quote it if it contains a colon.
---
```

`updated` is the field that tells you whether to trust a file. A stale date is worse than none, so the check script complains when a changed file does not carry today's date.

Notes made from a document or recording can carry provenance: `source` (where the original is), `extraction: ai` (an AI reading of it, not the original) and `verified: true` once you checked it against the original.

`summary` is English on purpose: Claude can read the one-line summaries of fifty notes to decide which to open, whatever language the bodies are in.

## Naming and links

- File names: kebab-case, no diacritics, no dates (`choose-a-laptop.md`). Day-bound notes are the exception: `2026-10-05-meeting-supplier.md`.
- Link with `[[note-name]]` only to notes that exist.
- A `README.md` in a project folder carries `aliases: [folder-name]` and is linked as `[[folder-name]]`, never `[[README]]`.
- One growing note per topic beats three linked ones. Merge instead of duplicating.

## The Friday review

`/weekly` (15 minutes): rewrite `now.md`, walk active projects, harvest open questions that moved or rotted, tick off tasks, empty the inbox. If you only keep one habit, keep this one.
