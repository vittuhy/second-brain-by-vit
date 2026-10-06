# Git and sync

Git gives you history, undo and a way to move the vault between devices. It is not mandatory, but without it a bad AI edit is hard to take back.

## Model: Git is the canonical state

When you use a remote, the **Git repository is the canonical state and history**, and every vault on a disk is a working copy of it: the PC with Obsidian, the phone with GitSync, a cloud agent's container. **The latest pushed commit is the canonical shared state.** Markdown is the data format, Obsidian a local interface, Claude (on any device) reasoning and operations, `vault-check.py` integrity validation. If you mostly work from a phone assistant that pushes changes, the PC is a replica, not the authority. In the default review-only mode with no remote, the folder on disk is the only copy.

Because several clients write to one state, **synchronisation is a safety boundary**:

1. Pull or sync the latest state before any change (`git fetch`, compare with `origin`).
2. If the remote is ahead and nothing overlaps, bring it in first. If histories diverge in a way that needs a choice, **stop and resolve it yourself**, the agent does not.
3. Make the change and run `python3 scripts/vault-check.py`.
4. Commit and push (only in a mode that allows it).

Never force push a personal vault, never silently resolve divergent histories, never push a stale working tree over newer remote changes, and never treat a cached clone as authoritative without checking where it stands against the remote.

## Who commits

Choose one mode (`/setup` records it under "Local setup" in `CLAUDE.md`):

| Mode | Behaviour | Pick it if |
|---|---|---|
| **Review only** (default) | The agent never commits. You read `git diff` and commit by hand. | You want control. Recommended for the first month. |
| **Agent commits locally** | The agent commits at the end of a task. You push. | You trust the checks and want less ceremony. |
| **Cloud agent** | Claude Code on the web commits and pushes straight to `main` of a **private** repository, usually from a phone. Your vault is cloned into a remote container and processed there. | You capture and process on the go and accept that privacy model (see below). |

Rules in every mode: never force push, never rewrite published history, commit message `area: what changed`, and the working tree must be clean before structural changes so the agent's work shows up cleanly in `git diff`.

## Desktop

Obsidian, Claude Code and the terminal all write to the same folder. Commit by hand:

```bash
git status
git diff
git add -A && git commit -m "triage: sort inbox" && git push
```

Run `git config pull.rebase true` once so a manual `git pull` does not ask about strategy.

## Mobile

Many people, the author included, work mostly from the phone: capture into the inbox, voice notes, quick edits, and Claude Code on the web for the heavy lifting. This is the setup that makes that work on **iOS**, and it is the recommended one.

### Recommended: GitSync plus an iOS Shortcut

**[GitSync](https://apps.apple.com/us/app/gitsync/id6744980427)** (App Store) is a native git client for iOS. Use it instead of the Obsidian Git plugin: the plugin runs a JavaScript git implementation that was seen to break on merges on iOS and get stuck without a way to abort, discard or reset. A native app handles merges and resets properly.

Setup, once:

1. Install GitSync and sign in to GitHub (OAuth, or a fine-grained token with *Contents: Read and write* on your private vault repository).
2. Clone your vault repository with GitSync into a folder Obsidian can open.
3. In Obsidian, open that folder as the vault.
4. Keep the **Obsidian Git plugin disabled** in this vault. Two git tools on one folder will fight.

Automate it, so you never think about syncing:

1. Open **Shortcuts**, then **Automation**, then **+** (new automation).
2. Choose **App**, select **Obsidian**, tick **Is Opened**.
3. Add the action **GitSync: Sync Now**.
4. Set it to **Run Immediately** and turn off *Notify When Run* / *Ask Before Running*.

**Ready-made shortcut.** The author shares the shortcut here: [add it from iCloud](https://www.icloud.com/shortcuts/6f7eeeaa49a243cabff0682be8c5bef3). As with any shortcut from the internet, open it in the Shortcuts app and read its actions before you add it. Note that iOS does not let you share a personal automation (the *When Obsidian is opened* trigger) by link, so you always create that part yourself and point it at the shortcut or at the **GitSync: Sync Now** action.

Now every time you open Obsidian, GitSync pulls what changed (for example what the cloud agent or your computer pushed) and pushes what you changed. Optionally add a second automation with **Is Closed** and the same action so your edits are pushed as you leave. "Closed" means leaving the app or sending it to the background, not force-quitting it from the app switcher.

Daily flow with the automation in place: open Obsidian (it syncs), capture or edit, close Obsidian (it syncs, if you added the second automation). Without the second automation, run **Sync Now** by hand after a long editing session.

Rules of thumb on the phone:

- Only capture into `inbox/` there. Do not move folders around on the phone; leave structural changes to `/triage` and `/weekly`.
- If you use a cloud agent, the same Sync Now pulls its commits in; a real same-line conflict is offered for manual resolution instead of wedging.
- Do not run bulk rewrites from the computer while you are mid-edit on the phone.

### Android and others

Not tested by the author. The Obsidian Git plugin is the common choice there; Syncthing or Obsidian's own paid Sync service are alternatives (Obsidian Sync does not give you git history). Treat these as starting points, not recommendations from experience.

## Cloud agent (optional)

Claude Code on the web can work on a repository from your phone. **It is a different privacy boundary from a local session, not just another git workflow.** The vault is cloned into a remote container, every file the agent reads is processed remotely, and a push creates a remote copy in your repository. Unlike a local agent it may also commit and push without you looking at `git diff` first. Compare the paths:

| Operation | Trust model |
|---|---|
| Read local files | Local agent access |
| Write local files | Agent mutation |
| Git commit | Persistent local history |
| Git push | Remote copy |
| GitSync | Additional remote and client copy |
| Cloud agent | Personal vault content processed remotely |

Enable it only when you understand this and have set `Cloud agent: enabled` in the privacy profile in `CLAUDE.md`. If you enable this mode:

1. The repository **must be private**, and GitHub secret scanning with push protection should be on (see [privacy.md](privacy.md)).
2. Before changing anything the agent runs `git fetch origin main`. If the remote has moved it rebases onto it, and **if that is not clean it stops and tells you**. Before pushing it runs `python3 scripts/vault-check.py`, and it never force pushes.
3. After a cloud push, your phone runs **Sync** and the change merges. A real conflict (same line edited on both sides) is offered for manual resolution.
4. Avoid bulk rewrites while you are mid-edit on the phone.

## When it goes wrong

- **Conflict:** pick the correct version in the git app or editor. Never force push a personal vault.
- **Last resort:** clone the repository again from the remote. Everything is on the remote.
- **Something deleted by mistake:** `git log -- path/to/file`, then `git checkout <commit>~1 -- path/to/file`.
- **Secret committed:** deleting it in a new commit does not help; the history keeps it. Rotate the secret. See [privacy.md](privacy.md).
