# Getting started

About 15 minutes from zero to a working second brain.

## What you need

| Tool | Why | Required |
|---|---|---|
| [Obsidian](https://obsidian.md) | The interface: reading, linking, Bases views, mobile | Yes (any Markdown editor works, but Bases and the widget are Obsidian features) |
| [Claude Code](https://code.claude.com) | The AI layer that reads the vault and runs the slash commands | Yes |
| Git | History, sync, undo | Strongly recommended |
| Python 3 and PyYAML | Runs `scripts/vault-check.py` | Yes (`pip install pyyaml`) |
| A voice recorder or assistant | Hands-free capture | Optional, see [voice-capture.md](voice-capture.md) |

## Step by step

### 1. Get your own private copy

**Do not fork this repository for personal use.** A fork of a public repository is public, and everything you write would be public with it.

1. Click **Use this template** on GitHub, then **Create a new repository**.
2. Set visibility to **Private**.
3. Clone your new repository:

```bash
git clone https://github.com/<you>/<your-repo>.git my-second-brain
cd my-second-brain
```

No GitHub account? Download the ZIP, unpack it, run `git init` and keep it local.

### 2. Open it in Obsidian

*Open folder as vault* and pick the folder. Obsidian may ask whether to trust the vault; the repository ships only core-plugin settings. If prompted, enable **Bases** (Settings, Core plugins).

### 3. Run the onboarding

In a terminal, in the vault folder:

```bash
pip install pyyaml
claude
```

Then in Claude Code:

```
/setup
```

Claude interviews you one question at a time (name, work, goals, what to enable, how git should work), then fills `context/`, removes the areas and collections you do not want and tailors `CLAUDE.md`. Answer "skip" to anything; edit the files later.

### 4. Check and commit

```bash
python3 scripts/vault-check.py
git add -A && git commit -m "setup: initial personal context"
```

### 5. Live with it for a week

- Dump things into `inbox/`. Do not sort them yourself.
- Run `/triage` when the inbox has a few items.
- `/morning` and `/evening` if they suit you.
- `/weekly` on Friday: this is the habit that keeps the system honest.
- `/context-sprint finance` (or health, work, relationships) when you have 20 minutes, to deepen one area.

## On the phone

If you mostly work from your phone, set up sync once: install [GitSync](https://apps.apple.com/us/app/gitsync/id6744980427), clone your vault with it, open that folder as the vault in Obsidian and add the Shortcuts automation *When Obsidian is opened, GitSync: Sync Now*. Details in [git-and-sync.md](git-and-sync.md).

## First thing to try

Create a file `inbox/idea.md` with a sentence of text. Run `/triage`. Claude gives it frontmatter, a name and a home, links it to related notes and tells you what it did. That loop is the whole system.

## Updating the template later

Your copy is yours. If the template improves, compare with it instead of merging blindly:

```bash
git remote add template https://github.com/<template-owner>/second-brain-by-vit.git
git fetch template
git diff HEAD template/main -- .claude scripts docs
```

Only take changes to `.claude/`, `scripts/` and `docs/`; never to your `context/` or `areas/`.
