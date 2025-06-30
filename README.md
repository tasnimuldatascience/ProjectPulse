# ProjectPulse MCP Server

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repo-blue)](https://github.com/tasnimuldatascience/ProjectPulse.git)

## 🚀 Overview

ProjectPulse is a fully functional [Model Context Protocol (MCP)](https://smithery.com/mcp) server designed to automate the job application process using AI. It leverages a Large Language Model (LLM) agent to dynamically generate personalized cover letters, populate Notion databases, and create formatted Google Docs—all from a single resume upload and job keyword input.

## 🧠 What is MCP?

MCP (Model Context Protocol) is a new open standard for AI that acts like a “USB‑C port for AI agents,” allowing them to securely interact with real-world tools (e.g., Notion, Google Docs, GitHub). ProjectPulse is designed to comply with this specification.

## ✅ Key Features

* **Resume Upload**: Upload a PDF or DOCX resume for semantic extraction.
* **LLM Agent**: Generates job-specific cover letters based on resume and job description.
* **Google Docs Integration**: Stores generated cover letters as Google Docs.
* **Notion Integration**: Tracks job applications in a Notion database.
* **OAuth Identity Handling**: Auth flows for both Google and Notion.
* **MCP Compliance**: Connects 3+ tools, respects user identity and permissions, and uses LLM agents.

---

## 🛠️ Tech Stack

* **Backend**: FastAPI
* **Frontend**: Streamlit
* **AI**: OpenAI GPT-based agent
* **Integrations**: Google Docs API, Notion API, RemoteOK job scraper
* **Auth**: Google OAuth 2.0 + Notion OAuth

---

## 📂 Folder Structure

```
ProjectPulse/
├── app/
│   ├── routes/
│   │   ├── job.py
│   │   ├── notion_auth.py
│   │   └── google_auth.py
│   ├── services/
│   │   ├── job_scraper.py
│   │   ├── google_docs_service.py
│   │   ├── notion_service.py
│   │   └── cover_letter_service.py
├── frontend/
│   └── app.py
├── main.py
├── .env
└── requirements.txt
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/tasnimuldatascience/ProjectPulse.git
cd ProjectPulse
```

### 2. Set Up Python Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file with the following:

```
OPENAI_API_KEY=your_openai_key
NOTION_CLIENT_ID=...
NOTION_CLIENT_SECRET=...
NOTION_REDIRECT_URI=http://localhost:8000/auth/notion/callback
GOOGLE_CLIENT_ID=...
GOOGLE_CLIENT_SECRET=...
GOOGLE_REDIRECT_URI=http://localhost:8000/auth/google/callback
NOTION_TOKEN=...
DATABASE_ID=...
GOOGLE_TOKEN=...
```

### 4. Run the Backend (FastAPI)

```bash
uvicorn main:app --reload
```

### 5. Run the Frontend (Streamlit)

```bash
streamlit run frontend/app.py
```

---

## 🌐 OAuth Integration

* 🔐 Google OAuth for Docs access: `/auth/google/login`
* 🔐 Notion OAuth for workspace access: `/auth/notion/login`

Tokens are securely stored and used for per-user context enforcement.

---

## 🧪 Example Workflow

1. Upload resume.
2. Enter job keyword (e.g., "Data Scientist").
3. LLM generates a cover letter.
4. Google Docs stores the letter.
5. Notion tracks the job application.

---

## 🧠 Agent Behavior

* Agent uses resume + job title + company name to generate cover letters.
* Follows prompt-engineered templates.
* Can be extended to support chain-of-thought or tool-using agents.

---

## 📈 Evaluation (Optional Bonus)

Future support for [`smithery.ai evals`](https://smithery.com/mcp/evals) to test how accurately the agent performs.

---

## 🧩 Contributions

Feel free to fork and extend with:

* Slack or GitHub integrations
* MongoDB or PostgreSQL backend
* Feedback loops for letter quality

---

## 📜 License

MIT License © [Tasnimul Hasan](https://github.com/tasnimuldatascience)

---

## 🌟 Credits

Built for the Headstarter Software Residency as an MCP-compatible full-stack AI application.
