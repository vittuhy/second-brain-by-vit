# Areas

An area is an ongoing responsibility with no end. `/setup` lets you pick which to keep.

| Area | Hub | What goes here |
|---|---|---|
| `people/` | one folder per person, hub named after them | People close to you: a hub, notes that concern only them, a log of your dated reflections |
| `health/` | `health.md` | Fitness, therapy, and medical history with one extraction per diagnosis |
| `finance/` | `finance.md` | Overview, taxes, insurance, loans |
| `home/` | `home.md` | Where you live, property you own, utilities |
| `gear/` | `gear.md` | What you own, wishlist, things to sell |
| `travel/` | `travel.md` | Reusable travel material |
| `work/` | `work.md` | Current role, work relationships, responsibilities |
| `vault/` | `vault.md` | The system itself: voice capture, ledger, roadmap |

## How an area grows

1. Start with the hub only. It is a map, not a container.
2. When a topic has content, create a note for it and link it from the hub.
3. When a topic gets its own folder and hub, add a line to "Where to start by topic" in `CLAUDE.md`.
4. Hubs link; they do not copy.

## People

`areas/people/<name>/<name>.md` is the hub. Create it from `templates/person.md`. Alongside it:

- notes that concern only that person,
- `reflections-on-<name>.md`: a growing log of dated entries in your own voice.

`context/people.md` stays the index of who is who. Your reflections about people close to you are yours to keep; decide once, in `CLAUDE.md`, whether the agent should ask before writing about them (the template asks for anyone outside your closest circle).

## Health

A new medical report **extends the existing note on the same diagnosis or body part**. Create a new note only for a new topic. The timeline in `medical-history.md` always gets a row. The originals stay outside the repository; see [privacy.md](privacy.md).

## Adding your own area

Make a folder in `areas/`, a hub note from `templates/area-hub.md` named after the folder, and a line in CLAUDE.md. Run `/health` afterwards to catch anything you missed.
