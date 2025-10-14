# Password Strength Checker (CLI · API · Web UI)

A **beginner-friendly** but **master’s-level** password strength evaluation toolkit.
It combines rule checks and an **entropy-based estimate** with pattern detection
(dictionary, keyboard sequences, repeated chars, dates, l33t substitutions).
You get:

- Python library (`passcheck`)
- CLI: `python -m passcheck "MyP@ssw0rd!" --json`
- REST API (FastAPI) with CORS
- Simple web UI that talks to the API
- Pytest unit tests
- GitHub Actions CI

> **Note**: This is an educational project. Don’t send real passwords to demo servers.

---

## Quick Start

### 1) Create & activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
```

### 2) Install

```bash
pip install -e .[dev]
```

### 3) CLI usage

```bash
python -m passcheck "P@ssw0rd123!" --json
```

### 4) Run the API

```bash
uvicorn api.main:app --reload
```

Open http://127.0.0.1:8000/docs for Swagger UI.

### 5) Web UI (static)

Open `web/index.html` in your browser **after** starting the API above.

### 6) Tests

```bash
pytest -q
```

---

## How it Works

- **Entropy Estimate**: `length * log2(pool_size)` where pool_size depends on present classes
  (lower/upper/digits/symbols). We subtract bits for risky patterns: common passwords,
  dictionary words (incl. l33t), keyboard/ascending sequences, dates, repeats.
- **Score** (0–100): nonlinear mapping of adjusted entropy plus bonuses for diversity and length.
- **Feedback**: actionable hints (e.g., “add another unique symbol”, “avoid years like 1998”).

### Strength Bands

- 0–24: Very weak
- 25–49: Weak
- 50–69: Fair
- 70–84: Strong
- 85–100: Excellent

---

## Project Layout

```
password-strength-checker/
├─ api/
│  └─ main.py
├─ src/passcheck/
│  ├─ __init__.py
│  ├─ __main__.py        # CLI
│  ├─ checks.py
│  ├─ entropy.py
│  ├─ feedback.py
│  ├─ score.py
│  └─ data/common_weak_passwords.txt
├─ tests/
│  └─ test_basic.py
├─ web/
│  ├─ index.html
│  └─ app.js
├─ pyproject.toml
├─ SECURITY.md
├─ LICENSE
└─ README.md
```

---

## Publish to GitHub (step‑by‑step)

```bash
# 1) Initialize git
git init
git add .
git commit -m "feat: initial release of password strength checker"

# 2) Create a new repo on GitHub (via web UI)
# 3) Add the remote (replace YOURUSER and REPO)
git remote add origin https://github.com/YOURUSER/password-strength-checker.git
git branch -M main
git push -u origin main
```

---

## Roadmap Ideas (stretch)

- Offline breach corpus check (k‑anonymity or bloom filter)
- UI with dynamic strength meter (no API roundtrip)
- Multi-language wordlists & keyboard layouts
- Markov/PCFG estimator for advanced modeling
- Browser extension or VS Code plugin
