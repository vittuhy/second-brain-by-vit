# Projects

A project is a **temporary outcome with a defined end**, usually a decision, a deliverable or a change. A decision project (the default workflow below) has a question, criteria and a deadline, and produces a basis for the decision. A project that delivers something (a migration, a launch, a physical change) states its outcome, a definition of done and a deadline instead, and does not need a decision model. Decisions made along the way still go to `context/decisions.md`.

## Starting one

```
/new-project choose-a-laptop
```

Claude checks the inbox for a brief, otherwise interviews you one question at a time to get:

1. **The question** the project answers.
2. **Four to six measurable criteria.** Written *before* collecting data, so the data cannot choose them.
3. **A deadline.**

It does not propose options until the criteria exist. Then it creates `projects/choose-a-laptop/README.md` from `templates/project.md`.

## While it runs

- **Chat is not storage.** Any calculation, comparison, quote or research that comes up in a conversation is written to a working note in the project folder (`calculations.md`, `candidates.md`...) and linked from the README under *Material*.
- One note per aspect. File names are unique across the vault (not `notes.md`).
- The README's *Status* section holds the current state and the next step or the gate.

## Closing

1. Record the outcome: a decision goes to `context/decisions.md` (append-only); a deliverable or change is recorded in the README (`status: closed`, `closed` date, what was delivered).
2. Move the folder to `archive/projects/`.

`/weekly` flags projects that look done and projects that have not moved in 60 days.
