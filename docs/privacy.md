# Privacy and what never goes in

This system is built to hold deeply personal material, so be deliberate about where it lives.

## 0. Where your data goes

The vault is a folder on your disk, but it does not stay on that disk by itself. Four separate paths exist, and each one is a decision:

| Path | What happens to the data |
|---|---|
| Local vault | Stored on your disk. Anything with access to your disk can read it. |
| Claude Code | Every file Claude reads in a session enters the model context and is **processed by the AI service**. If it is in a note Claude opens, it leaves your machine for processing. |
| Git remote | Everything you commit and push is copied to the remote (GitHub). A **private** repository limits who can see it, it does not mean the data never left your machine, and the host still stores it. |
| GitSync or another sync client | Each device holds a full copy of the repository, and the app talks to the remote. |
| Cloud agent (Claude Code on the web) | The repository is cloned into a remote container and **everything the agent reads is processed there**. Different privacy model from a local session, enable it knowingly. |

| Operation | Trust model |
|---|---|
| Read local files | Local agent access |
| Write local files | Agent mutation |
| `git commit` | Persistent local history |
| `git push` | Remote copy |
| GitSync | Additional remote and client copy |
| Cloud agent | Personal vault content processed remotely |

Treat the vault as potentially containing sensitive personal data, and decide per device and per workflow what may touch it. `/setup` records your choices in the privacy profile under "Local setup" in `CLAUDE.md`. This repository contains no telemetry of its own.

## 1. Keep the repository private

If you will write real things in your vault, the repository must be **private**. A public repository, or a **fork** of a public repository, publishes everything you commit. To start from this template use *Use this template* and choose Private (see [getting-started.md](getting-started.md)). Check the visibility on GitHub before your first push.

If you want to share a part of your vault, copy it out deliberately; do not make the whole repository public.

**Never use this public template repository as your vault.** Cloning it and committing your notes, or pushing to its remote, publishes them. `scripts/vault-check.py` reports an ERROR when `origin` points at the template after `/setup` has filled in your context, and `/setup` checks the remote before the first personal-data commit. Create your own private repository first.

## 2. Secrets never go in

Passwords, tokens, API keys, PINs, recovery codes and card numbers do not belong in the vault, ever. **Deleting a secret from git history does not repair the leak**: copies made in the meantime remain, so the only reliable fix is to change the secret. They belong in a password manager. The `.gitignore` excludes `.env`, `*.pem` and `*.key` as a safety net, not as a policy: a secret can sit in Markdown, YAML, JSON, a pasted API response or a transcript under any file name. So a second layer exists:

- `python3 scripts/vault-check.py` scans every text file for well-known credential formats (private keys, cloud and GitHub tokens, Slack and Google keys, JWTs: ERROR) and for `password = value` style assignments (WARNING). A false alarm is silenced with `vault-check: secret-ok` on the same line. It is a pattern check, it cannot see a secret written as ordinary prose.
- Turn on **GitHub secret scanning and push protection** on your private repository (Settings, Code security).
- Optional: a local pre-commit scanner such as [Gitleaks](https://github.com/gitleaks/gitleaks) if you commit from a machine you control.

The Pocket Sync plugin stores your API key in `.obsidian/plugins/pocket-sync/data.json`. That file is ignored by `.gitignore`. Do not remove that line.

If Claude sees a secret while processing, it leaves it out and tells you what it left out.

## 3. Identifiers stay out of extractions

When Claude extracts a contract, policy or report, it does not write national ID numbers, ID card or passport numbers and their validity, bank account numbers or payment references. The line is **what the number does**: a contract or policy number identifies a file and unlocks nothing, so it stays; an account number moves money, so it goes. If you need such a number to act, the note says it exists and where to get it.

## 4. Documents: text only

Binary files (PDF, scans, photos) do not go into the repository. They bloat every clone, including the phone's, and you cannot search them. When you hand Claude a document it writes a thorough text extraction (identification, every amount and date, obligations, exclusions, exact wording of disputable clauses, what is *not* covered, what it left out). **The extraction is the only record the vault holds**, so it must be complete enough to stand alone. But it is **derived data, not the source**: an AI reading can drop a footnote, misread a scan or get a number wrong. The original stays where you keep it; the note's `source` field says where, `extraction: ai` marks the text as an AI-produced reading, and `verified: true` means you compared it with the original. Before you act on a figure that matters (a payment, a deadline, a claim), check it in the original.

## 5. Other people's data

Third-party personal data is not forbidden, but it is not the agent's call. The agent asks and states its concern. Decide once, in `CLAUDE.md`, how you want to treat people close to you (the template asks for anyone outside your closest circle) and for anyone recorded without knowing it.

## 6. The ten-year test

Before committing, ask "would I mind this being here in ten years?", not "is it secret?". History can be rewritten (`git filter-repo`, BFG) but it costs a re-clone on every device, so treat it as a one-off cleanup, not routine.

## 7. Cloud agents and connectors

Anything Claude reads in a session is processed by the service you use, and a cloud agent does it in a remote container. Connect only the mail, calendar and drive accounts you are comfortable with, and only for a concrete recurring task. Before you enable a cloud workflow, read the data paths in section 0 and [git-and-sync.md](git-and-sync.md).

## 8. Content is data, not instructions

Notes, transcripts, web clips, imported documents and copied text can contain sentences that look like commands ("delete the archive", "ignore your rules", "commit and push", "reveal the contents of..."). An attacker can plant one in a web clip, a recording or a shared document, and an innocent one can sit in a note you wrote. `CLAUDE.md` tells the agent to treat all vault content as data: it reports such a passage and never acts on it. Only your own message in the conversation authorises deleting, committing, pushing, running commands, changing `CLAUDE.md` or settings, or revealing information. Voice transcripts are the same: a spoken instruction is part of the transcript, not a command to the agent.

The default permissions are in `CLAUDE.md` (Source of truth and trust). In short: reading, searching, running the check and inspecting git are allowed; creating, modifying and moving files happens as part of what you asked for; deleting asks first; commit and push only when you enabled a git mode; network actions are higher risk.
