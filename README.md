<p align="center">
  <img src="assets/second-brain-logo.png" alt="Second Brain by Vit" width="200">
</p>

<h1 align="center">Second Brain by Vit</h1>

<p align="center">
  A Git-native personal knowledge system, operated through AI, for <a href="https://obsidian.md">Obsidian</a> and <a href="https://code.claude.com">Claude Code</a>.<br>
  Plain Markdown in a Git repository. Git is the canonical state. Claude is the librarian. Chat is not storage.
</p>

---

## What is this?

An empty, ready-to-use skeleton of a personal second brain. No data, no opinions about your life, only structure, rules and routines that I have found to work:

- **A folder system with a routing rule for every file**: inbox, context, areas, projects, collections, notes, sources, archive.
- **Context files Claude reads before it advises you**: who you are, what you want, what is happening now, how you decide.
- **Nine slash commands** for the daily, weekly and yearly rhythm, including an **onboarding interview** (`/setup`) that fills it all in with you.
- **Obsidian Bases views** for books, films, places and recipes, plus a recipe for your own.
- **Voice capture**: talk to a recorder or assistant, and the transcript is filed into the right notes. Reference setup: Pocket AI.
- **A check script** that keeps the vault consistent as an AI edits it.
- **Rules for documents and privacy**: extract contracts and reports into text (marked as AI-derived, with the original as the source), keep secrets out, keep binaries out, and a clear map of where your data goes.

Everything is Markdown and YAML. It survives any app, model or service.

## Quick start

> **Use a private copy.** Do not fork this repository for personal use: a fork of a public repo is public, and so is everything you write in it.

1. Click **Use this template**, then **Create a new repository**, visibility **Private**.
2. Clone it and open the folder in Obsidian (*Open folder as vault*).
3. In a terminal inside the folder:

   ```bash
   pip install pyyaml
   claude
   ```

4. In Claude Code, run:

   ```
   /setup
   ```

5. Answer the questions (about ten minutes, one at a time, you can skip any). Claude fills in your context, removes the areas you do not want, and tailors the rules.
6. Run `python3 scripts/vault-check.py`, then commit.

More detail: [docs/getting-started.md](docs/getting-started.md).

### What `/setup` does

It checks your environment, warns you if this copy could become public, then interviews you about the basics, how you decide, your goals, which areas and collections to enable, whether you use a voice recorder, how git should behave and which devices you use. It shows a plan, waits for your yes, writes the files and runs the check. It never overwrites context you have already written without asking.

## How the vault is organised

```
inbox/         new, unsorted capture. A queue, not a home
context/       who I am, what I want, what is happening, how I decide, tasks, open questions
areas/         ongoing responsibilities: people, health, finance, home, gear, travel, work, vault
projects/      decisions with an end: question, criteria, deadline, working notes
collections/   lists you filter and sort (books, films, places, recipes) with Bases views
notes/         loose thoughts and findings
sources/       verbatim material (voice transcripts); never edited
archive/       inactive material
templates/     note templates
docs/          guides for the system itself
scripts/       vault-check.py
.claude/       slash commands and the /setup skill
CLAUDE.md      the rules Claude follows in this repository
```

| Folder | Test: does it belong here? |
|---|---|
| `inbox/` | Anything new. Down to zero every Friday. |
| `context/` | What Claude must know before it advises me. |
| `collections/` | An item in a list I want to filter and sort. |
| `projects/` | A decision with an end that produces a basis for it. |
| `areas/` | A lasting responsibility. |
| `notes/` | A thought or finding with no responsibility and no list. |
| `sources/` | A verbatim source. Not knowledge. |
| `archive/` | No longer valid, but I do not want to delete it. |

Nothing lives in two folders at once. See [docs/how-it-works.md](docs/how-it-works.md).

## The core ideas

1. **Git is the canonical state, Markdown is the data.** If it matters, it is in a file in the repository. Local vaults are working copies of it, and the latest pushed commit is the canonical shared state. Chat is not storage.
2. **A few context files do the heavy lifting.** `about-me`, `goals`, `now` and `decisions`. `now.md` carries an `updated` date; if it is older than 14 days Claude says so and does not trust it.
3. **Every note is one of three things**: a fact (a note), an action (`context/tasks.md`) or an open question (`#open-question` in a note). Never the same thing in two places.
4. **Every file carries frontmatter** (`title`, `type`, `created`, `updated`, `tags`, `summary`) and a script checks it. `updated` is bumped whenever the content changes, so a stale date is a signal.
5. **One growing note beats three linked ones.** Merge instead of duplicating.
6. **The agent asks, you decide.** It never deletes more than five files unasked, never decides a piece of content "does not belong", and never commits unless you enabled it.
7. **Content is data, not instructions.** Notes, transcripts, web clips and imported documents can contain text that looks like a command. The agent never obeys it, only you can authorise an action.

## Daily, weekly, yearly

| Command | What it does |
|---|---|
| `/setup` | First-run onboarding interview |
| `/morning` | One-minute brief from `now.md`, goals, inbox, calendar |
| `/evening` | Two-minute shutdown into the daily note |
| `/triage` | Sorts the inbox, adds frontmatter, links notes, flags duplicates, files voice transcripts |
| `/weekly` | Friday review: rewrite `now.md`, walk projects, open questions, tasks, inbox |
| `/new-project <name>` | Starts a project (a decision, a deliverable or a change) with its end defined first |
| `/context-sprint <area>` | 15 to 20 minute interview that fills a thin area |
| `/health` | Vault health report; changes nothing |
| `/yearly` | Reviews the transcript archive once a year |

Details and a suggested rhythm: [docs/commands.md](docs/commands.md).

## Areas

`people`, `health`, `finance`, `home`, `gear`, `travel`, `work` and the always-on `vault`. Each starts with a hub note that links, never copies. `/setup` removes the ones you decline; you can add your own. People close to you get a folder with a hub and a log of your dated reflections. Medical reports extend the existing note on the same diagnosis. See [docs/areas.md](docs/areas.md).

## Collections and Bases

Books, films, places and recipes ship with templates and `.base` views (tables and cards, filtered by status, rating, time). Bases is a core Obsidian feature (1.9 or newer). Adding your own collection is four steps. See [docs/collections-and-bases.md](docs/collections-and-bases.md).

## Voice capture

Speak, and the transcript becomes notes. The vault accepts anything that leaves a `transcript.md` in `inbox/Conversations/<date>/<title>/`. The reference setup is the [Pocket](https://heypocket.com) recorder with the **Pocket Sync** community plugin for Obsidian.

The pipeline: record, sync into the inbox, `/triage` reads the transcript (never trusting the summary's dates), saves it verbatim to `sources/transcripts/`, writes the content into notes with links back to the exact passage, classifies each action item as task, open question, content or noise, logs it in a ledger and cleans the inbox. Includes the pitfalls found in practice (why deleted folders reappear, the two look-alike settings, what a full re-scan does). See [docs/voice-capture.md](docs/voice-capture.md).

## Documents and privacy

- **The vault is text.** Binary attachments do not go in. Give Claude a contract, policy or report and it writes a complete extraction: identification, every amount and date, obligations, exclusions, exact wording, what the document does *not* cover. The extraction is the only record Claude will have.
- **Secrets never go in**: passwords, tokens, keys, PINs, card numbers. Deleting them from history does not repair the leak.
- **Identifiers stay out of extractions**: ID and passport numbers, bank accounts. Contract and policy numbers stay.
- **Extractions are derived data.** The original is the source; a note says `extraction: ai` and whether you verified it.
- **Keep the repository private** if it holds personal data, and never use this public template as your vault.
- **Know where your data goes.** The vault is local, but Claude processes every file it reads, a Git remote and a sync app hold copies, and a cloud agent processes the vault remotely.
- **Content is data, not instructions**, so a transcript or web clip cannot make the agent delete, commit or push.

Full policy: [docs/privacy.md](docs/privacy.md).

## Git and sync

By default **the agent never commits**: you review `git diff` and commit by hand. When you use a remote, the Git repository is the canonical state and every vault is a working copy, so sync comes before any change and a force push is never the answer. Optional modes let the agent commit locally or work from the cloud on a private repository. **Working mostly from the phone?** The recommended iOS setup is the native git app [GitSync](https://apps.apple.com/us/app/gitsync/id6744980427) plus one iOS Shortcut automation: *When Obsidian is opened* run *GitSync: Sync Now*. Your vault then pulls and pushes by itself every time you open Obsidian, and a cloud agent can work on the same repository in between. A ready-made shortcut is linked there too. Step by step, and what failed with the alternatives, in [docs/git-and-sync.md](docs/git-and-sync.md).

## The check script

```bash
python3 scripts/vault-check.py
```

Read-only. It reports ERROR (exit code 1) and WARNING for: missing frontmatter fields, invalid YAML, `updated` in the future or earlier than `created`, changed files whose `updated` is not today (compared against the same path in `HEAD`), folder READMEs without an alias, ambiguous `[[README]]`, duplicate file names, broken wikilinks, wikilinks in the task list, transcripts without a `keep` value, invalid `extraction` or `verified` values, likely secrets in any text file, and an `origin` that points to this public template. Claude runs it after every change.

## Requirements

- Obsidian 1.9 or newer (for Bases)
- Claude Code
- Python 3 and PyYAML
- Git (recommended)

## Documentation

| Guide | Contents |
|---|---|
| [Getting started](docs/getting-started.md) | Install and first run |
| [How it works](docs/how-it-works.md) | Principles, routing, frontmatter, naming |
| [Areas](docs/areas.md) | Areas and people |
| [Collections and Bases](docs/collections-and-bases.md) | Lists and views |
| [Projects](docs/projects.md) | Projects with an end |
| [Commands](docs/commands.md) | Slash commands and rhythm |
| [Voice capture](docs/voice-capture.md) | Recorders, Pocket, transcripts |
| [Git and sync](docs/git-and-sync.md) | Commit modes, mobile, cloud |
| [Privacy](docs/privacy.md) | What never goes in |
| [Customising](docs/customising.md) | Make it yours |
| [Troubleshooting](docs/troubleshooting.md) | Common problems |

## FAQ

**Do I need Claude Code?** The structure works in any Markdown editor. The routines, the interview and the consistency checks are built for Claude Code.

**Can I write in my own language?** Yes. Keep the `summary` line in English, or change that rule (see [docs/customising.md](docs/customising.md)).

**Is anything sent anywhere?** The vault is stored on your disk, but not only there. Claude Code processes every file it reads in a session, so that content goes to the AI service. A Git remote receives everything you push, GitSync adds another copy on each device, and a cloud agent processes your vault in a remote container. Treat the vault as potentially sensitive personal data. This repository contains no telemetry of its own. Details and a trust table: [docs/privacy.md](docs/privacy.md).

**Why not a notes app with a database?** The tool should not own your knowledge. Plain text outlives apps.

## Contributing

Issues and pull requests that make the skeleton more general are welcome. Please never include personal data in an issue or PR. A change to a rule in `CLAUDE.md` must come with the matching change in `scripts/vault-check.py` and the commands.

## Credits

Built by Vit Tuhy. The Pocket Sync plugin is by its own author; Pocket, Obsidian and Claude are products of their respective companies, and this project is not affiliated with them.

## License

[MIT](LICENSE)
