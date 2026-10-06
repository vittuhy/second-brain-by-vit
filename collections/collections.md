---
title: Collections
type: context
created: 2026-10-05
updated: 2026-10-05
tags: [meta, collections]
summary: How collections work and how to add a new one with its own Base view
---
# Collections

A collection is a list you want to filter and sort: books, films, places, recipes. One file per item, one Base per collection. The Base reads the frontmatter of the files in its folder and shows them as a table or cards.

## Adding an item

Create a note from the matching template in `templates/` (the Web Clipper or Claude can fill it in). Fill every property the template has. The Base only shows what the frontmatter holds.

## Adding a new collection

1. Create `collections/<name>/`.
2. Create a template `templates/<name>.md` with the properties you want to filter on.
3. Copy one of the existing `.base` files into the folder and change the folder in `file.inFolder(...)`, the property names and the view names.
4. Add the new `type` to `NO_SUMMARY_TYPES` in `scripts/vault-check.py` only if items are clipped automatically and cannot carry a summary.

Trigger for a new collection: you have more than about ten items of one kind sitting in `notes/`. Not before.

Full syntax of `.base` files: https://obsidian.md/help/bases/syntax
