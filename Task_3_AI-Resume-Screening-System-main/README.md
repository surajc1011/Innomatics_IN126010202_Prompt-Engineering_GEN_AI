# 🤖 AI Resume Screening System
### GenAI Assignment – LangChain + LangSmith Tracing

---

## 📌 Overview

An AI-powered resume screening system that evaluates candidates against a job description using a **5-step LangChain pipeline** with full **LangSmith tracing**.

**Pipeline Flow:**
```
Resume → Skill Extraction → JD Matching → Scoring (0-100) → Explanation → LangSmith Trace
```

---

## 🗂️ Project Structure

```
ai_resume_screener/
│
├── main.py                    ← Main entry point (run this)
├── AI_Resume_Screener.ipynb   ← Jupyter Notebook version
├── requirements.txt           ← Dependencies
├── .env                       ← API keys (fill this in)
│
├── prompts/
│   └── templates.py           ← All PromptTemplate definitions
│
├── chains/
│   └── pipeline.py            ← LCEL chains + full pipeline function
│
├── data/
│   └── resumes.py             ← 3 sample resumes + job description
│
└── outputs/
│   └── screening_results.json ← Auto-generated results
└── Screenshots/               ← Langsmith project_overview 
```

---

## ⚙️ Setup Instructions

### 1. Clone / Download the Project
```bash
git clone https://github.com/YOUR_USERNAME/ai-resume-screener.git
cd ai_resume_screener
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure API Keys
Edit the `.env` file:
```env
GROQ_API_KEY=your-groq-api-key-here
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
LANGCHAIN_API_KEY=ls__your-langsmith-api-key-here
LANGCHAIN_PROJECT=AI-Resume-Screener
```

**Get your keys:**
- Groq: https://console.groq.com/keys
- LangSmith: https://smith.langchain.com → Settings → API Keys

### 4. Run the Project
```bash
python main.py
```
Or open `AI_Resume_Screener.ipynb` in Jupyter/VS Code.

---

## 🔬 Pipeline Steps

| Step | Description | LangChain Component |
|------|-------------|---------------------|
| 1 | **Skill Extraction** – Parse resume for skills, experience, tools | `PromptTemplate` + `LCEL` |
| 2 | **JD Parsing** – Extract job requirements | `PromptTemplate` + `LCEL` |
| 3 | **Matching** – Compare candidate vs job | `PromptTemplate` + `LCEL` |
| 4 | **Scoring** – Assign 0-100 score with breakdown | `PromptTemplate` + `LCEL` |
| 5 | **Explanation** – Generate hiring recommendation | Few-shot `PromptTemplate` + `LCEL` |

---

## 📊 Scoring Criteria

| Category | Max Points |
|----------|-----------|
| Required Skills Coverage | 35 |
| Experience Match | 25 |
| Tools / Tech Stack | 20 |
| Education & Achievements | 10 |
| Preferred / Bonus Skills | 10 |
| **Total** | **100** |

**Grades:** A (80-100) | B (60-79) | C (40-59) | D (<40)

---

## 🔍 LangSmith Tracing

4 traced runs appear in your LangSmith dashboard:

1. `Resume Screening – Strong Candidate` (tag: `strong`)
2. `Resume Screening – Average Candidate` (tag: `average`)
3. `Resume Screening – Weak Candidate` (tag: `weak`)
4. `DEBUG – Incomplete Resume Input` (tag: `debug`) ← demonstrates debugging

View at: https://smith.langchain.com → Your Project

---

## ✅ Assignment Checklist

- [x] 3 resumes (Strong / Average / Weak)
- [x] 1 Job Description (Data Scientist)
- [x] Skill Extraction (Step 1)
- [x] Matching Logic (Step 2-3)
- [x] Scoring 0-100 (Step 4)
- [x] Explanation with reasoning (Step 5)
- [x] LangChain LCEL (`prompt | llm | parser`)
- [x] Modular structure (`prompts/`, `chains/`, `main.py`)
- [x] LangSmith tracing (`LANGCHAIN_TRACING_V2=true`)
- [x] Minimum 3 LangSmith runs
- [x] Debug run for incorrect output
- [x] Few-shot prompting (Step 5)
- [x] No hardcoded outputs
- [x] No hallucinated skills
- [x] Clean, modular, commented code

---

## 🛠️ Technologies Used

- **Python 3.10+**
- **LangChain** – Pipeline orchestration, LCEL, PromptTemplates
- **LangSmith** – Tracing, debugging, monitoring
- **Groq Mixtral 8x7B** – Fast & free LLM backbone
- **python-dotenv** – Environment management

---

## 👤 Author

**Atharv Jadhav  
Data Science Intern – February 2026 Innomatics  
LinkedIn: https://www.linkedin.com/in/atharv--jadhav/  
GitHub: https://github.com/atharvjadhav1112
