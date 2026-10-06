# Collections and Bases

A **collection** is a list of things you want to filter and sort. A **Base** is an Obsidian view (a `.base` file) that turns the frontmatter of the notes in a folder into a table or cards. No plugin is needed: Bases is a core Obsidian feature (version 1.9 or newer; enable it under Settings, Core plugins).

## What ships

| Collection | Template | Base views |
|---|---|---|
| `collections/books/` | `templates/book.md` | Want to read, Read |
| `collections/films/` | `templates/film.md` | Want to watch, Watched, Cards |
| `collections/places/` | `templates/place.md` | All places, Want to visit |
| `collections/recipes/` | `templates/recipe.md` | All recipes, Quick and proven, Cards |

## Using one

1. Create a note from the template (`Insert template` in Obsidian, or ask Claude).
2. Fill the properties. `status: want` or `done`/`seen`, `rating`, and so on.
3. Open the `.base` file in the same folder. The note appears in the matching view.

Claude can fill items from a URL or a title; the Obsidian Web Clipper can map a page onto a template's properties. Items from the clipper may lack a `summary`; the check script allows that for `film`, `book` and `place`.

## Creating your own

See `collections/collections.md`. In short: new folder, new template, copy a `.base` file and change the folder and the properties.

A minimal Base:

```yaml
filters:
  and:
    - file.inFolder("collections/wines")
    - file.ext == "md"
views:
  - type: table
    name: All wines
    order:
      - file.name
      - grape
      - rating
```

## Gotchas

- Property names in filters must match the frontmatter exactly. `displayName` only changes the column heading.
- A property that is empty in the frontmatter (`rating:`) is fine; one that is missing from the template never appears as a column choice.
- On mobile, Bases views render but are read-heavy; capture new items into `inbox/` and let `/triage` file them.
- Full syntax: [Obsidian Bases syntax](https://obsidian.md/help/bases/syntax).
