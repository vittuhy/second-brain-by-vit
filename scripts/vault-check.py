#!/usr/bin/env python3
"""Vault check: frontmatter, dates, links, duplicate names.

Run by the agent after every change (see CLAUDE.md) and by /health. Only reads, changes nothing.

    python3 scripts/vault-check.py            # whole vault
    python3 scripts/vault-check.py file.md    # only selected files (links and duplicates are always checked vault-wide)

Exit code 1 when there is at least one ERROR. WARNINGs do not change the exit code.
Requires PyYAML (pip install pyyaml).
"""
import datetime as dt
import pathlib
import re
import subprocess
import sys
from collections import defaultdict

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
TODAY = dt.date.today()

# Folders where frontmatter is not checked: feed, archive, templates, docs, tooling.
SKIP_FM = ("archive/", "templates/", "docs/", "assets/", "inbox/Conversations/", "inbox/Archive/",
           "inbox/Insights/", ".claude/", ".git/", "scripts/", ".obsidian/", ".trash/")
# Structural root files without frontmatter.
SKIP_FILES = {"README.md", "CLAUDE.md", "LICENSE.md", "CONTRIBUTING.md"}
REQUIRED = ["title", "type", "created", "updated", "tags", "summary"]
# Items clipped automatically cannot always carry a summary.
NO_SUMMARY_TYPES = {"film", "book", "place"}
# Files in the inbox are still being triaged, missing fields are only warnings.
LENIENT = ("inbox/",)

errors, warnings = [], []


def err(path, msg):
    errors.append(f"ERROR    {path}: {msg}")


def warn(path, msg):
    warnings.append(f"WARNING  {path}: {msg}")


def rel(p):
    return p.relative_to(ROOT).as_posix()


def all_files():
    out = []
    for p in ROOT.rglob("*"):
        r = rel(p)
        if p.is_file() and not r.startswith((".git/", ".obsidian/", ".trash/")):
            out.append(p)
    return out


def parse_date(v):
    if isinstance(v, dt.date):
        return v
    if isinstance(v, str) and re.fullmatch(r"\d{4}-\d{2}-\d{2}", v.strip()):
        return dt.date.fromisoformat(v.strip())
    return None


_head_blobs = None


def _git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, timeout=10)


def git_dirty(r):
    """Content changed against HEAD. A pure move or rename does not count."""
    global _head_blobs
    try:
        if not _git("status", "--porcelain", "--", r).stdout.strip():
            return False
        blob = _git("hash-object", "--", r).stdout.strip()
        head = _git("rev-parse", "--verify", "-q", f"HEAD:{r}")
        if head.returncode == 0:
            # The path exists in HEAD: compare against exactly HEAD:<path>, not against the content of other files.
            return blob != head.stdout.strip()
        # The path does not exist in HEAD (new or moved file): a move is recognised by identical content elsewhere in HEAD.
        if _head_blobs is None:
            tree = _git("ls-tree", "-r", "HEAD").stdout
            _head_blobs = {line.split()[2] for line in tree.splitlines() if line}
        return blob not in _head_blobs
    except Exception:
        return False


def check_frontmatter(p):
    r = rel(p)
    text = p.read_text(encoding="utf-8")
    report = warn if r.startswith(LENIENT) else err
    if not text.startswith("---\n"):
        report(r, "missing frontmatter")
        return
    end = text.find("\n---", 4)
    if end == -1:
        err(r, "unterminated frontmatter")
        return
    try:
        fm = yaml.safe_load(text[4:end]) or {}
    except yaml.YAMLError as e:
        err(r, f"invalid YAML in frontmatter ({str(e).splitlines()[0]}); quote any value that contains a colon")
        return
    if not isinstance(fm, dict):
        err(r, "frontmatter is not a mapping")
        return
    required = [k for k in REQUIRED if not (k == "summary" and fm.get("type") in NO_SUMMARY_TYPES)]
    missing = [k for k in required if fm.get(k) in (None, "", [])]
    if missing:
        report(r, "missing " + ", ".join(missing))
    created, updated = parse_date(fm.get("created")), parse_date(fm.get("updated"))
    for k, v in (("created", created), ("updated", updated)):
        if fm.get(k) not in (None, "") and v is None:
            err(r, f"{k} is not in YYYY-MM-DD format: {fm.get(k)!r}")
    if updated and updated > TODAY:
        err(r, f"updated {updated} is in the future")
    if created and updated and updated < created:
        err(r, f"updated {updated} is earlier than created {created}")
    if fm.get("extraction") not in (None, "ai", "manual"):
        err(r, f"extraction must be 'ai' or 'manual', got {fm.get('extraction')!r}")
    if fm.get("verified") not in (None, True, False):
        err(r, f"verified must be true or false, got {fm.get('verified')!r}")
    # A changed, uncommitted file must have today as `updated`. Git history is not checked,
    # mass mechanical edits (renaming links) would cause false alarms.
    if updated and updated != TODAY and git_dirty(r):
        err(r, f"file is changed but updated is {updated}, not today")
    if p.name == "README.md":
        folder = p.parent.name
        if folder not in (fm.get("aliases") or []):
            err(r, f"folder README needs aliases: [{folder}], otherwise [[README]] is ambiguous")
    if r.startswith("sources/") and fm.get("keep") not in ("permanent", "review"):
        err(r, "transcript needs keep: permanent or keep: review")
    if r == "context/tasks.md":
        for i, line in enumerate(text.splitlines(), 1):
            if line.lstrip().startswith("- [") and "[[" in line:
                err(r, f"line {i}: wikilink in a task (the widget cannot render it)")


SECRET_ERR = [
    ("private key", re.compile(r"-----BEGIN (?:RSA |EC |DSA |OPENSSH |PGP )?PRIVATE KEY")),
    ("AWS access key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("GitHub token", re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{36}\b|\bgithub_pat_[A-Za-z0-9_]{22,}")),
    ("Anthropic or OpenAI key", re.compile(r"\bsk-(?:ant-)?[A-Za-z0-9_-]{32,}")),
    ("Slack token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}")),
    ("Google API key", re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b")),
    ("JWT", re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}")),
]
SECRET_WARN = [
    ("password, token or key assigned a value",
     re.compile(r"(?i)\b(?:password|passwd|secret|api[_-]?key|access[_-]?token|auth[_-]?token)\b[\"']?\s*[:=]\s*[\"']?(?!<|\{|\$|x{3}|\*{3}|your|example|changeme|placeholder)[^\s\"'`]{8,}")),
]
TEXT_SUFFIXES = {".md", ".txt", ".json", ".yaml", ".yml", ".toml", ".ini", ".cfg", ".env", ".sh", ".py", ".js", ".csv", ".base", ".canvas"}
SECRET_SELF = "scripts/vault-check.py"


def check_secrets(files):
    """Pattern scan of every text file. A safety net, not a guarantee: it cannot see a secret that looks like prose."""
    for p in files:
        r = rel(p)
        if p.suffix.lower() not in TEXT_SUFFIXES and p.name not in {".env"} or r == SECRET_SELF:
            continue
        try:
            lines = p.read_text(encoding="utf-8", errors="ignore").splitlines()
        except OSError:
            continue
        for n, line in enumerate(lines, 1):
            if "vault-check: secret-ok" in line:
                continue
            hit = False
            for what, rx in SECRET_ERR:
                if rx.search(line):
                    err(r, f"looks like a secret ({what}), line {n}. Secrets do not belong in the vault: rotate it and remove it from the text")
                    hit = True
                    break
            if hit:
                continue
            for what, rx in SECRET_WARN:
                if rx.search(line):
                    warn(r, f"possible secret ({what}), line {n}. Check it; mark a false alarm with a 'vault-check: secret-ok' comment on the same line")
                    break


def check_remote():
    """Personal data must not be committed to a clone of the public template."""
    try:
        url = _git("remote", "get-url", "origin").stdout.strip()
    except Exception:
        return
    if "second-brain-by-vit" not in url.lower():
        return
    about = ROOT / "context" / "about-me.md"
    # The untouched template itself legitimately points here. Once /setup has filled the context, it must not.
    if about.exists() and "Name, year of birth, where you live, languages." in about.read_text(encoding="utf-8"):
        return
    err(".git", f"origin points to the public template ({url}). Personal data would end up in a public repository. Create your own PRIVATE repository and repoint origin before the first commit")


def strip_code(text):
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", text)


def main(argv):
    files = all_files()
    md = [p for p in files if p.suffix == ".md"]
    targets = [ROOT / a for a in argv] if argv else md

    for p in targets:
        r = rel(p)
        if p.suffix != ".md" or r.startswith(SKIP_FM) or (p.parent == ROOT and p.name in SKIP_FILES):
            continue
        check_frontmatter(p)

    # Names a link can point to: basename without .md, path, other files with extension, aliases.
    names, by_base = set(), defaultdict(list)
    for p in files:
        r = rel(p)
        if p.suffix == ".md":
            names.add(p.stem.lower())
            names.add(r[:-3].lower())
            by_base[p.stem.lower()].append(r)
            try:
                t = p.read_text(encoding="utf-8")
                if t.startswith("---\n"):
                    fm = yaml.safe_load(t[4:t.find("\n---", 4)]) or {}
                    for a in (fm.get("aliases") or []) if isinstance(fm, dict) else []:
                        names.add(str(a).lower())
            except Exception:
                pass
        else:
            names.add(p.name.lower())
            names.add(r.lower())

    for base, paths in sorted(by_base.items()):
        live = [x for x in paths if not x.startswith(("archive/", "templates/", "inbox/", ".claude/", "docs/"))]
        if len(live) > 1 and base != "readme":
            warn(", ".join(live), f"same file name '{base}', [[{base}]] is ambiguous")

    for p in md:
        r = rel(p)
        if r.startswith(("archive/", "templates/", "inbox/", ".claude/", "docs/")) or r in SKIP_FILES:
            continue
        for m in re.finditer(r"!?\[\[([^\]|#^]+)", strip_code(p.read_text(encoding="utf-8"))):
            # Inside a table an alias is written [[target\|text]], the backslash is not part of the target.
            target = m.group(1).strip().rstrip("\\").lower()
            if target.endswith(".md"):
                target = target[:-3]
            if target and target not in names:
                err(r, f"broken link [[{m.group(1).strip()}]]")
            elif target == "readme":
                err(r, "link [[README]] is ambiguous, link to the folder alias")

    check_secrets(files)
    check_remote()

    for line in errors + warnings:
        print(line)
    print(f"\n{len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
