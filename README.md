# git relax or auto git

Automatically commits and pushes your code to GitHub every time you save a file. No terminal juggling, no manual `git add / commit / push`. Just code and hit Cmd+S.

---

## How it works

A Python script using `watchdog` monitors your project folder in the background. The moment a file save is detected, it runs:

```
git add <filename>  →  git commit -m "auto: update <filename>"  →  git push
```

3-second debounce built in — so rapid saves don't spam your commit history.

---

## Setup (macOS)

**1. Create the tools folder and virtual environment**
```bash
mkdir -p ~/tools && cd ~/tools
python3 -m venv venv
source venv/bin/activate
pip install watchdog
```

**2. Save the script**
```bash
nano ~/tools/auto_git.py
```
Paste the contents of `auto_git.py`, then `Ctrl+O` → Enter → `Ctrl+X`.

**3. Add a global alias**
```bash
nano ~/.zshrc
```
Add this line:
```bash
alias auto-git="~/tools/venv/bin/python3 ~/tools/auto_git.py"
```
Then reload:
```bash
source ~/.zshrc
```

---

## Usage

Navigate to any git-initialized project folder and run:

```bash
auto-git .
```

Leave that terminal tab running. Every save now auto-commits and pushes.

To stop it: `Ctrl+C`

---

## Prerequisites

Before running `auto-git` on a project, make sure it's a git repo with a remote connected:

```bash
git init
git remote add origin https://github.com/yourusername/repo.git
git branch -M main
git push -u origin main
```

Check if remote already exists:
```bash
git remote -v
```

---

## What gets ignored

The watcher skips these automatically:

- `.git/`
- `__pycache__/`
- `.pyc` files
- `.DS_Store`
- `node_modules/`
- `.ipynb_checkpoints/`

---

## Heads up

- Commit history will be noisy (`auto: update main.py` × 40). Fine for personal projects and hackathons.
- For shared or showcase repos, work on a `dev` branch and merge to `main` manually when ready.
- The script needs to keep running in a terminal tab — it's not a background daemon (yet).

---

## Stack

- Python 3.8+
- [watchdog](https://github.com/gorakhargosh/watchdog)
- Git (obviously)

---

Built for the "I just want to code without thinking about Git" workflow.
