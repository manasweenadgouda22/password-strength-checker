# 🔐 Password Strength Checker — FastAPI · Render · GitHub Pages

### 🚀 Live Demo Links

| Component | Status | Link |
|------------|--------|------|
| 🌐 **Frontend (Web UI)** | ✅ Live | [https://manasweenadgouda22.github.io/password-strength-checker/](https://manasweenadgouda22.github.io/password-strength-checker/) |
| ⚙️ **API Endpoint** | ✅ Live | [https://password-strength-checker-1inv.onrender.com/evaluate](https://password-strength-checker-1inv.onrender.com/evaluate) |
| 📘 **API Docs (Swagger UI)** | ✅ Live | [https://password-strength-checker-1inv.onrender.com/docs](https://password-strength-checker-1inv.onrender.com/docs) |

---

## 💡 Overview

A **beginner-friendly yet master’s-level** end-to-end security tool that evaluates password strength using both **statistical entropy** and **pattern-based analysis**.

Users can:
- ✅ Test password strength via an intuitive web UI  
- ✅ Access a REST API for automated evaluation  
- ✅ Run checks from the CLI for local testing  

This project demonstrates full-stack development and deployment — from Python packaging to cloud deployment and static hosting.

---

## 🧠 Features

- 🧩 **FastAPI backend** with `/evaluate` and `/healthz` endpoints  
- 🔐 **Entropy-based scoring system** + pattern detection:
  - Common passwords
  - Dictionary/l33t substitutions
  - Keyboard or numeric sequences
  - Repeated characters
  - Date/year patterns  
- ⚙️ **Frontend (HTML + JS)** with real-time meter visualization  
- 🧪 **Pytest** unit testing suite  
- 💡 **CI/CD with GitHub Actions**  
- ☁️ **Deployed on Render + GitHub Pages**

---

## 🧰 Tech Stack

| Layer | Technology |
|-------|-------------|
| Backend | FastAPI, Uvicorn |
| Frontend | HTML5, CSS3, JavaScript (Fetch API) |
| Language | Python 3 |
| Deployment | Render (Backend) + GitHub Pages (Frontend) |
| Testing | Pytest |
| CI/CD | GitHub Actions |

---

## 🏗️ Architecture Overview
User → Web UI (GitHub Pages)
↓ Fetch API
Backend (FastAPI on Render)
↓
Entropy + Rule Engine (Python)
↓
JSON Response to UI


---

## 🧪 Run Locally

```bash
# 1️⃣ Create & activate virtual environment
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate

# 2️⃣ Install dependencies
pip install -e .[dev]

# 3️⃣ Run API
uvicorn api.main:app --reload

# 4️⃣ Open API docs
http://127.0.0.1:8000/docs

# 5️⃣ Launch Web UI
Open web/index.html in your browser

⚙️ CLI Mode
python -m passcheck "P@ssw0rd123!" --json
Returns:

{
  "strength": "Excellent",
  "score": 100,
  "entropy_bits_adjusted": 94.87,
  "feedback": ["Avoid dictionary words or common phrases—even with l33t substitutions."]
}

API Reference
| Method | Endpoint    | Description                    |
| ------ | ----------- | ------------------------------ |
| `POST` | `/evaluate` | Returns password strength JSON |
| `GET`  | `/healthz`  | Health check endpoint          |
| `GET`  | `/docs`     | Swagger documentation          |

🧩 Project Structure

password-strength-checker/
├── api/
│   └── main.py
├── src/passcheck/
│   ├── __init__.py
│   ├── __main__.py
│   ├── checks.py
│   ├── entropy.py
│   ├── feedback.py
│   ├── score.py
│   └── data/common_weak_passwords.txt
├── tests/
│   └── test_basic.py
├── docs/
│   ├── index.html
│   └── app.js
├── .github/workflows/ci.yml
├── LICENSE
├── README.md
├── SECURITY.md
├── pyproject.toml
└── requirements.txt

🌈 Future Enhancements

🔍 Offline breached password lookup (k-anonymity model)

🌐 Multi-language wordlists & keyboard patterns

🧠 Advanced ML-based scoring (Markov / PCFG)

🧩 Browser extension or VS Code plugin



