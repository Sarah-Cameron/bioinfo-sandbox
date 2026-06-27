# SPEC — Bioinformatics Sandbox (Binder repo)

A build spec for an agent (e.g. Claude Code) to generate or extend this repository.
Hand this file to the agent and say "build the repo described in SPEC.md".

## Goal

A **zero-install, browser-based** teaching environment for beginning bioinformatics
students. One click on a Binder launch link opens a real Linux container running
JupyterLab, giving students (a) a Python notebook and (b) a true **bash terminal**
(`cd`, `ls`, run scripts, edit files), plus a few classic command-line bioinformatics
tools. Hosted free from a public GitHub repo via https://mybinder.org. No student
accounts, no local installs.

## Non-goals

- Not persistent: Binder sessions reset after ~10 min idle. Do not build features
  that assume saved state.
- Not a graded-exam platform: mybinder.org is best-effort community infra. (Note in
  docs that Codespaces / self-hosted BinderHub are the path for guaranteed capacity.)
- No web server, database, or backend code. Everything is static repo content +
  Binder config.

## Target audience for the *content*

Absolute beginners to the command line. Examples must be tiny, readable, and heavily
commented. Favour clarity over cleverness.

## Repository layout

```
.
├── README.md             # Launch badge + publish/customise instructions (human-facing)
├── SPEC.md               # This file (agent-facing)
├── environment.yml       # Binder build definition — the primary knob
├── postBuild             # Executable; one-time build-step setup
├── intro.ipynb           # Guided first notebook
├── BASH_CHEATSHEET.md    # ~15 essential commands
├── scripts/
│   └── count_bases.py    # Small worked example
└── data/
    └── sample.fasta      # Tiny sample dataset
```

## File specifications

### `environment.yml`  (REQUIRED — this is what Binder reads)
- Conda environment file. Channels: `conda-forge`, then `bioconda`.
- Pin Python (`python=3.11`).
- Must include `jupyterlab>=4` — this provides BOTH notebooks and the bash terminal.
- Teaching stack: `numpy`, `pandas`, `matplotlib`, `biopython`, `pip`.
- CLI bioinformatics tools: `samtools`, `seqkit` (from bioconda). Mark in a comment
  that these can be removed to speed up builds.
- Keep it LEAN — every dependency adds to build time. Comment liberally.

### `postBuild`  (optional but included)
- Bash script, must be committed **executable** (`chmod +x`, or
  `git update-index --chmod=+x postBuild`).
- Runs ONCE at image build time, not per launch.
- Here: `chmod +x scripts/*.py` so students can run `./scripts/...`. Use
  `set -e`. Keep idempotent and tolerant (`|| true`).

### `intro.ipynb`  (REQUIRED)
- Valid nbformat 4 notebook. Python 3 kernel (`python3`).
- Structure, in order:
  1. Markdown: welcome; explain the two modes (notebook vs Terminal via
     File ▸ New ▸ Terminal); warn that work is temporary — download to keep.
  2. Python cell: print hello + compute GC content of an inline sequence.
  3. Markdown + cell: shell commands via `!` (`!pwd`, `!ls -la`, `!head data/...`).
  4. Cell: `!python scripts/count_bases.py data/sample.fasta`.
  5. Cell: `!seqkit stats data/sample.fasta` (demonstrates a CLI tool).
  6. Markdown: "your turn" — a copy-pasteable terminal exercise + pointer to the
     cheatsheet.
- All code cells must have `"outputs": []` and `"execution_count": null`.

### `BASH_CHEATSHEET.md`  (REQUIRED)
- A markdown table of ~15–18 commands: `pwd ls ls -la cd cd .. cd ~ cat head tail
  less mkdir cp mv rm nano python grep wc`. One-line plain-English descriptions.
- A "try this sequence" block and a "make and run your own script" block.

### `scripts/count_bases.py`  (REQUIRED example)
- Pure standard library (no third-party imports) so it always runs.
- Reads a FASTA file given as `argv[1]`; prints per-sequence length + GC%, then totals.
- Include a module docstring showing both invocation forms. Usage error → exit 1.
- Heavily readable; this is example code students will copy.

### `data/sample.fasta`  (REQUIRED)
- 3 short FASTA records with descriptive headers. ~35–125 bp each. Plain ACGT.

### `README.md`  (REQUIRED — human-facing)
- Binder launch badge:
  `[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/USER/REPO/HEAD?urlpath=lab/tree/intro.ipynb)`
  with a clear instruction to replace `USER/REPO`.
- The plain launch URL to give students, plus a terminal-first variant
  (`?urlpath=terminals/1`).
- Table of repo contents.
- 5-step "How to publish" (public repo → upload → edit badge → first launch builds
  & caches).
- "Customising" (add deps to environment.yml; trim tools for speed; add lessons).
- "Things to tell students" (work is temporary; first load is slow; not guaranteed
  capacity).

## Binder mechanics the agent must respect

- The launch URL form is `https://mybinder.org/v2/gh/<user>/<repo>/<branch-or-HEAD>?urlpath=...`.
- Config files live in repo root (or a `binder/` subdir, but root is simpler here).
- `environment.yml` is the canonical dependency file; do not also add `requirements.txt`
  unless intentionally needed (avoid conflicting config).
- First launch after a commit triggers a multi-minute rebuild; subsequent launches are
  cached. Don't design around instant startup.

## Acceptance checks (agent should self-verify)

1. `find . -type f` shows the layout above.
2. `python3 scripts/count_bases.py data/sample.fasta` runs and prints per-seq + totals.
3. `python3 -c "import json; json.load(open('intro.ipynb'))"` succeeds (valid notebook).
4. `python3 -c "import yaml; yaml.safe_load(open('environment.yml'))"` succeeds and
   includes `jupyterlab`.
5. `postBuild` is executable and starts with a shebang.
6. README badge/link contain the `USER/REPO` placeholder (not a hardcoded repo).

## Extension ideas (optional, if asked)

- Add `aligning.ipynb` using Biopython pairwise alignment on `data/sample.fasta`.
- Add a `binder/runtime.txt` or `apt.txt` only if a tool needs system packages.
- Add `nbgitpuller` links so students can pull updated lessons without re-launching.
- For a real class, document migration to GitHub Codespaces (`.devcontainer`) or a
  self-hosted BinderHub.
```
