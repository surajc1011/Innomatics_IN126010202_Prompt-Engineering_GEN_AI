"""
╔══════════════════════════════════════════════════════════════════════════════╗
║           AI Resume Screening System – main.py                             ║
║           Built with LangChain + LangSmith Tracing                         ║
╚══════════════════════════════════════════════════════════════════════════════╝

Pipeline Flow:
  Resume ──► Skill Extraction ──► JD Matching ──► Scoring ──► Explanation
                                                              └──► LangSmith Trace

Usage:
  python main.py

Requirements:
  - .env file with OPENAI_API_KEY and LANGCHAIN_* keys configured
  - pip install -r requirements.txt
"""

import os
import json
from dotenv import load_dotenv
from langsmith import traceable

# Load environment variables (API keys + LangSmith config)
load_dotenv()

# ── Validate required environment variables ───────────────────────────────────
def validate_env():
    required = ["GROQ_API_KEY", "LANGCHAIN_API_KEY"]
    missing = [k for k in required if not os.getenv(k)]
    if missing:
        raise EnvironmentError(
            f"\n❌ Missing environment variables: {missing}"
            f"\n   Please fill in your .env file before running."
        )
    tracing = os.getenv("LANGCHAIN_TRACING_V2", "false")
    print(f"✅ LangSmith Tracing Enabled: {tracing}")
    print(f"✅ LangSmith Project: {os.getenv('LANGCHAIN_PROJECT', 'default')}")
    print(f"✅ Using Groq API\n")

# ── Imports (after env loaded) ────────────────────────────────────────────────
from chains.pipeline import build_llm, run_screening_pipeline
from data.resumes import RESUMES, JOB_DESCRIPTION


# ─────────────────────────────────────────────────────────────────────────────
# LangSmith @traceable decorator: each call becomes a separate trace run
# You will see these as individual runs in your LangSmith dashboard
# ─────────────────────────────────────────────────────────────────────────────

@traceable(name="Resume Screening – Strong Candidate", tags=["strong", "data-scientist"])
def screen_strong_candidate(llm):
    resume = RESUMES["strong"]
    return run_screening_pipeline(
        resume_text=resume["text"],
        candidate_name=resume["name"],
        job_description=JOB_DESCRIPTION,
        llm=llm,
    )


@traceable(name="Resume Screening – Average Candidate", tags=["average", "data-scientist"])
def screen_average_candidate(llm):
    resume = RESUMES["average"]
    return run_screening_pipeline(
        resume_text=resume["text"],
        candidate_name=resume["name"],
        job_description=JOB_DESCRIPTION,
        llm=llm,
    )


@traceable(name="Resume Screening – Weak Candidate", tags=["weak", "data-scientist"])
def screen_weak_candidate(llm):
    resume = RESUMES["weak"]
    return run_screening_pipeline(
        resume_text=resume["text"],
        candidate_name=resume["name"],
        job_description=JOB_DESCRIPTION,
        llm=llm,
    )


# ─────────────────────────────────────────────────────────────────────────────
# DEBUG RUN: Intentional bad input to demonstrate LangSmith debugging
# This uses a deliberately empty/vague resume to show how the system handles it
# ─────────────────────────────────────────────────────────────────────────────

INTENTIONALLY_BAD_RESUME = """
Name: Test User
I know computers. I have done some projects.
I am a hard worker.
"""

@traceable(name="DEBUG – Incomplete Resume Input", tags=["debug", "error-case"])
def screen_debug_case(llm):
    """
    This run intentionally uses a poor/incomplete resume.
    Purpose: Demonstrate LangSmith tracing for debugging incorrect/unexpected outputs.
    Expected: Low score, system should NOT hallucinate skills.
    """
    return run_screening_pipeline(
        resume_text=INTENTIONALLY_BAD_RESUME,
        candidate_name="Debug Test User",
        job_description=JOB_DESCRIPTION,
        llm=llm,
        verbose=True,
    )


# ─────────────────────────────────────────────────────────────────────────────
# Output formatting
# ─────────────────────────────────────────────────────────────────────────────

def print_results(result: dict, level_label: str):
    """Pretty-print the screening results for one candidate."""
    sep = "═" * 70
    print(f"\n{sep}")
    print(f"  📋 CANDIDATE: {result['candidate_name']}  [{level_label}]")
    print(sep)

    print("\n📌 CANDIDATE PROFILE (Extracted):")
    print(result["candidate_profile"])

    print("\n📌 MATCH ANALYSIS:")
    print(result["match_analysis"])

    print("\n📌 SCORING BREAKDOWN:")
    print(result["scoring_details"])

    print(f"\n🏆 FINAL SCORE: {result['total_score']} / 100   |   GRADE: {result['grade']}")

    print("\n📌 EXPLANATION & RECOMMENDATION:")
    print(result["explanation"])
    print()


def save_results_to_json(all_results: list, output_path: str = "outputs/screening_results.json"):
    """Save all results to a JSON file for submission/review."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\n💾 Results saved to: {output_path}")


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

def main():
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║        AI Resume Screening System – Powered by LangChain        ║")
    print("╚══════════════════════════════════════════════════════════════════╝\n")

    # Validate env before anything else
    validate_env()

    # Build the LLM (llama-3.3-70b-versatile is faster and has great free tier)
    print("🔧 Initializing LLM (Llama 3.3 70B)...")
    llm = build_llm(model="llama-3.3-70b-versatile", temperature=0.0)
    print("✅ LLM ready.\n")

    all_results = []

    # ── Run 1: Strong Candidate ───────────────────────────────────────────────
    print("━" * 60)
    print("🚀 RUN 1: Screening STRONG candidate...")
    result_strong = screen_strong_candidate(llm)
    print_results(result_strong, "STRONG")
    all_results.append({**result_strong, "level": "Strong"})

    # ── Run 2: Average Candidate ──────────────────────────────────────────────
    print("━" * 60)
    print("🚀 RUN 2: Screening AVERAGE candidate...")
    result_avg = screen_average_candidate(llm)
    print_results(result_avg, "AVERAGE")
    all_results.append({**result_avg, "level": "Average"})

    # ── Run 3: Weak Candidate ─────────────────────────────────────────────────
    print("━" * 60)
    print("🚀 RUN 3: Screening WEAK candidate...")
    result_weak = screen_weak_candidate(llm)
    print_results(result_weak, "WEAK")
    all_results.append({**result_weak, "level": "Weak"})

    # ── Run 4: Debug Case (Intentional bad input) ─────────────────────────────
    print("━" * 60)
    print("🐛 RUN 4 (DEBUG): Screening incomplete/bad resume input...")
    print("   Purpose: Demonstrate LangSmith debugging for incorrect outputs")
    result_debug = screen_debug_case(llm)
    print_results(result_debug, "DEBUG CASE")
    all_results.append({**result_debug, "level": "Debug"})

    # ── Summary Table ─────────────────────────────────────────────────────────
    print("\n" + "═" * 70)
    print("  📊 SCREENING SUMMARY")
    print("═" * 70)
    print(f"  {'Candidate':<25} {'Level':<10} {'Score':>8}   {'Grade'}")
    print("  " + "-" * 55)
    for r in all_results:
        print(f"  {r['candidate_name']:<25} {r['level']:<10} {r['total_score']:>8}   {r['grade']}")
    print("═" * 70)

    # ── Save to JSON ──────────────────────────────────────────────────────────
    save_results_to_json(all_results)

    print("\n✅ All runs complete! Check your LangSmith dashboard for traces:")
    print(f"   https://smith.langchain.com/  → Project: {os.getenv('LANGCHAIN_PROJECT', 'AI-Resume-Screener')}")


if __name__ == "__main__":
    main()
