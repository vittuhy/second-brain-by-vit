# Customising

The template is deliberately small. Change what does not fit.

## Language

Notes can be in any language. Keep `summary` in English if you want cross-language search to work the same, or change that rule: edit the Writing rules in `CLAUDE.md`, the `REQUIRED` fields and messages in `scripts/vault-check.py`, and the instructions in `.claude/commands/`. Rules and script change together.

## Areas

Delete the ones you do not need (`/setup` does it for you), add your own (see [areas.md](areas.md)). Keep the line in "Where to start by topic" in sync.

## Collections

See [collections-and-bases.md](collections-and-bases.md).

## Templates

Edit `templates/`. Obsidian's core Templates plugin inserts them (`{{date:YYYY-MM-DD}}` is filled in on insert). If you add a property, existing notes keep working; Bases simply show it empty.

## The checker

`scripts/vault-check.py` encodes the rules in `CLAUDE.md`. If you add a required field, a note type that needs no summary (`NO_SUMMARY_TYPES`) or a folder to skip (`SKIP_FM`), change it there.

## Commands

Edit the Markdown in `.claude/commands/`. Rewording the commands is the cheapest way to make the system yours.

## Themes and plugins

Not included, on purpose: they are personal and often carry their own licences. Install what you like from Settings. `.obsidian/workspace.json` and per-plugin `data.json` are git-ignored because they are per-device state.

## Daily notes

Daily notes go to `inbox/` as `YYYY-MM-DD Daily note` (set in `.obsidian/daily-notes.json`). They are raw capture; `/triage` moves the useful parts out. Change the folder if you prefer a journal that stays put.

## Other AI tools

`CLAUDE.md` is read by Claude Code. Other agents read different files (for example `AGENTS.md`). You can add a one-line file that points to `CLAUDE.md`, or a symlink. The slash commands are Claude Code specific.
