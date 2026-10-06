# Commands

Slash commands live in `.claude/commands/` and run in Claude Code (`/name`). They are plain Markdown instructions; read and edit them freely.

| Command | What it does | When |
|---|---|---|
| `/setup` | First-run onboarding interview; fills context, enables areas, tailors CLAUDE.md | Once, at the start |
| `/morning` | Short brief from `now.md`, goals, inbox and calendar; sets the day's focus | Weekday mornings |
| `/evening` | Two-minute shutdown (done / left / tomorrow) into today's daily note | Evenings |
| `/triage` | Sorts `inbox/` by the routing rules, links notes, flags duplicates, processes voice conversations | When the inbox grows; after `/weekly` |
| `/weekly` | Friday review: rewrite `now.md`, walk projects, open questions, tasks, inbox | Friday, 15 minutes |
| `/new-project <name>` | Starts a project from a brief or by interview | A new project with a defined end |
| `/context-sprint <area>` | 15 to 20 minute interview that fills a thin area | Ad hoc |
| `/health` | Vault health report; changes nothing except saving the report | About monthly |
| `/yearly` | Reviews the transcript archive once a year | Once a year |

## Suggested rhythm

- **Morning:** `/morning`, pick one to three things.
- **Evening:** `/evening`.
- **Friday:** `/weekly`, then `/triage` if the inbox is full.
- **Monthly:** `/health`, re-read `goals.md`.
- **Yearly:** `/yearly`.

## Nudges

Commands do not run by themselves. If you tend to skip rituals, schedule a reminder (a phone alarm, a calendar event, or a scheduled Claude routine) that says "run /weekly". Do not schedule `/triage` rigidly; run it when the inbox has grown.

## Writing your own

Create `.claude/commands/<name>.md` with a `description` in frontmatter and plain instructions. Keep it short, one job, and end with the shared finishing line: run `python3 scripts/vault-check.py`, fix every ERROR, then commit only if CLAUDE.md allows it. Use `$ARGUMENTS` for what the user types after the name.

## Skills vs commands

`/setup` is a skill (`.claude/skills/setup/SKILL.md`) because it carries a long procedure that Claude should also pick up on its own when the context file is still the empty template. The rest are commands. Both are typed the same way.
