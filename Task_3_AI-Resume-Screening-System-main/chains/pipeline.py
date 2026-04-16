# ─────────────────────────────────────────────────────────────────────────────
# chains/pipeline.py  –  LangChain LCEL pipeline chains
# ─────────────────────────────────────────────────────────────────────────────

from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

from prompts.templates import (
    SKILL_EXTRACTION_PROMPT,
    JD_EXTRACTION_PROMPT,
    MATCHING_PROMPT,
    SCORING_PROMPT,
    EXPLANATION_PROMPT,
)


def build_llm(model: str = "llama-3.3-70b-versatile", temperature: float = 0.0) -> ChatGroq:
    """
    Initialize the LLM.
    temperature=0 ensures deterministic, consistent scoring outputs.
    """
    return ChatGroq(model=model, temperature=temperature)


# ─── Individual Chains (LCEL: prompt | llm | parser) ─────────────────────────

def get_skill_extraction_chain(llm: ChatGroq):
    """Chain 1: Extract skills/experience/tools from a resume."""
    return SKILL_EXTRACTION_PROMPT | llm | StrOutputParser()


def get_jd_extraction_chain(llm: ChatGroq):
    """Chain 2: Extract requirements from a job description."""
    return JD_EXTRACTION_PROMPT | llm | StrOutputParser()


def get_matching_chain(llm: ChatGroq):
    """Chain 3: Match candidate profile against job requirements."""
    return MATCHING_PROMPT | llm | StrOutputParser()


def get_scoring_chain(llm: ChatGroq):
    """Chain 4: Score the candidate based on match analysis."""
    return SCORING_PROMPT | llm | StrOutputParser()


def get_explanation_chain(llm: ChatGroq):
    """Chain 5: Generate human-readable explanation and hiring recommendation."""
    return EXPLANATION_PROMPT | llm | StrOutputParser()


# ─── Helper: Parse score from scoring output ─────────────────────────────────

def parse_total_score(scoring_output: str) -> str:
    """Extract TOTAL_SCORE and GRADE from scoring chain output."""
    total_score = "N/A"
    grade = "N/A"
    for line in scoring_output.splitlines():
        if line.startswith("TOTAL_SCORE:"):
            total_score = line.split(":", 1)[1].strip()
        if line.startswith("GRADE:"):
            grade = line.split(":", 1)[1].strip()
    return total_score, grade


# ─── Full Pipeline Function ───────────────────────────────────────────────────

def run_screening_pipeline(
    resume_text: str,
    candidate_name: str,
    job_description: str,
    llm: ChatGroq,
    verbose: bool = True,
) -> dict:
    """
    Runs the complete 5-step resume screening pipeline for one candidate.

    Steps:
        1. Extract skills from resume
        2. Extract requirements from JD
        3. Match candidate vs requirements
        4. Score the candidate (0-100)
        5. Generate explanation + recommendation

    Returns a dict with all step outputs.
    """

    results = {"candidate_name": candidate_name}

    # ── Step 1: Skill Extraction ──────────────────────────────────────────────
    if verbose:
        print(f"\n  [Step 1] Extracting skills for {candidate_name}...")
    skill_chain = get_skill_extraction_chain(llm)
    candidate_profile = skill_chain.invoke({"resume_text": resume_text})
    results["candidate_profile"] = candidate_profile

    # ── Step 2: JD Requirement Extraction ────────────────────────────────────
    if verbose:
        print("  [Step 2] Extracting job requirements...")
    jd_chain = get_jd_extraction_chain(llm)
    job_requirements = jd_chain.invoke({"job_description": job_description})
    results["job_requirements"] = job_requirements

    # ── Step 3: Matching ──────────────────────────────────────────────────────
    if verbose:
        print("  [Step 3] Matching candidate profile to job requirements...")
    match_chain = get_matching_chain(llm)
    match_analysis = match_chain.invoke({
        "candidate_profile": candidate_profile,
        "job_requirements": job_requirements,
    })
    results["match_analysis"] = match_analysis

    # ── Step 4: Scoring ───────────────────────────────────────────────────────
    if verbose:
        print("  [Step 4] Scoring the candidate...")
    score_chain = get_scoring_chain(llm)
    scoring_details = score_chain.invoke({
        "match_analysis": match_analysis,
        "job_requirements": job_requirements,
    })
    results["scoring_details"] = scoring_details

    total_score, grade = parse_total_score(scoring_details)
    results["total_score"] = total_score
    results["grade"] = grade

    # ── Step 5: Explanation ───────────────────────────────────────────────────
    if verbose:
        print("  [Step 5] Generating explanation and recommendation...")
    explain_chain = get_explanation_chain(llm)
    explanation = explain_chain.invoke({
        "candidate_name": candidate_name,
        "total_score": total_score,
        "grade": grade,
        "match_analysis": match_analysis,
        "scoring_details": scoring_details,
    })
    results["explanation"] = explanation

    return results
