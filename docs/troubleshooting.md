# Troubleshooting

**`vault-check.py` says ModuleNotFoundError: yaml.** Run `pip install pyyaml`.

**"invalid YAML in frontmatter".** A value contains a colon. Wrap it in quotes: `summary: "Plan: phase one"`.

**"file is changed but updated is ..., not today".** You edited a file without bumping `updated`. Set it to today's date. Files you did not touch are never flagged, and committed files are not checked against git history.

**"folder README needs aliases".** A `README.md` in a project folder must have `aliases: [folder-name]`.

**"broken link [[x]]".** No note called `x` exists. Create it or fix the link. Links to notes you plan to write later cause this, so do not write them.

**Open questions list is empty when Claude reads `open-questions.md`.** Expected: that file holds a query only Obsidian renders. Claude searches for `#open-question`.

**A Bases view is empty.** The folder in `file.inFolder("...")` must match; property names must match the frontmatter exactly; Bases must be enabled in Core plugins and Obsidian must be 1.9 or newer.

**Pocket conversations keep coming back after deletion.** See [voice-capture.md](voice-capture.md): turn off "Update existing notes on re-sync", and rely on the ledger.

**The widget shows a weird first line in `tasks.md`.** The file must start with a section heading and tasks, not a title. Keep the explanation at the bottom.

**Claude seems to ignore my context.** Check `now.md`: if older than 14 days Claude is told to distrust it. Check `about-me.md` is not still the empty template.

**Claude created a duplicate note.** Tell it to merge, and say which one wins. `/health` lists likely duplicates.

**Claude wants to delete many files.** It must ask above five. Say no, then ask for the list.

**I want to start over.** Delete the contents of `context/` and `areas/` hubs you filled, restore from git (`git checkout <first-commit> -- context areas`) and run `/setup` again.
