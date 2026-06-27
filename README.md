# Bioinformatics Sandbox (Binder)

A zero-install, browser-based Linux environment for students learning the **bash command line** and **simple Python scripting**. One click launches a real container with JupyterLab — notebooks *and* a true bash terminal — plus a few classic command-line bioinformatics tools.

## 🚀 Launch it

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Tancata/bioinfo-sandbox/HEAD?urlpath=lab/tree/intro.ipynb)

> The badge and links below are already wired to **`Tancata/bioinfo-sandbox`**. If you fork or rename this repo, replace that `USER/REPO` portion with your own GitHub username and repository name.

Direct link to give students:
`https://mybinder.org/v2/gh/Tancata/bioinfo-sandbox/HEAD?urlpath=lab/tree/intro.ipynb`

Want students to land straight in a **terminal** instead of the notebook? Use:
`https://mybinder.org/v2/gh/Tancata/bioinfo-sandbox/HEAD?urlpath=lab/tree/BASH_CHEATSHEET.md`
(then File ▸ New ▸ Terminal), or append `?urlpath=terminals/1` for a raw terminal.

## 📦 What's in this repo

| File | Purpose |
|---|---|
| `environment.yml` | Defines the environment Binder builds (Python + tools). **The one file you'll edit most.** |
| `postBuild` | Runs once at build time; makes scripts executable. |
| `intro.ipynb` | Guided first notebook — Python, shell commands, the sample script. |
| `BASH_CHEATSHEET.md` | The ~15 commands students need on day one. |
| `scripts/count_bases.py` | A small, readable example script (GC content from FASTA). |
| `data/sample.fasta` | Tiny sample dataset to practise on. |

## 🛠️ How to publish (5 minutes)

1. Create a new **public** GitHub repo.
2. Upload all these files (keep the folder structure: `scripts/`, `data/`).
3. Edit the badge/link in this README to point at your repo.
4. Visit your launch link once yourself — the **first** launch triggers a build (2–5 min). After that it's cached and fast for students.

That's it. No server to run, no accounts for students, free.

## ✏️ Customising

- **Add Python packages or CLI tools:** add a line under `dependencies:` in `environment.yml` (conda-forge or bioconda packages). Commit, then re-launch to rebuild.
- **Faster builds:** delete `samtools`/`seqkit` from `environment.yml` if you only need bash + Python.
- **Add your own lessons:** drop more `.ipynb` files or data in and point the launch link at them.

## ⚠️ Things to tell students

- **Work is temporary.** Sessions shut down after ~10 minutes of inactivity and everything resets. Download anything worth keeping (right-click ▸ Download).
- **Be patient on first load.** If nobody has launched recently, it rebuilds — give it a few minutes.
- **Public capacity, not guaranteed.** mybinder.org is a free community service. For a graded class running simultaneously, consider running your own [BinderHub](https://binderhub.readthedocs.io/) or GitHub Codespaces.

## 📚 References

- Binder: https://mybinder.org/  ·  Docs: https://mybinder.readthedocs.io/
- Configuration files reference: https://mybinder.readthedocs.io/en/latest/using/config_files.html
