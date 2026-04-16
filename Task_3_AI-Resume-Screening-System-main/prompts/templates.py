# ─────────────────────────────────────────────────────────────────────────────
# prompts/templates.py  –  All PromptTemplates for the pipeline
# ─────────────────────────────────────────────────────────────────────────────

from langchain_core.prompts import PromptTemplate

# ─── STEP 1: Skill Extraction ─────────────────────────────────────────────────
SKILL_EXTRACTION_PROMPT = PromptTemplate(
    input_variables=["resume_text"],
    template="""You are an expert resume parser.
Extract information ONLY from the resume provided below. Do NOT assume or infer skills not explicitly mentioned.

Resume:
{resume_text}

Extract and return the following in this exact format:

SKILLS: [comma-separated list of technical skills found in the resume]
EXPERIENCE_YEARS: [total years of professional experience as a number, 0 if fresher]
TOOLS: [comma-separated list of tools, frameworks, platforms mentioned]
EDUCATION: [highest degree and field]
KEY_ACHIEVEMENTS: [up to 3 notable achievements, or "None" if not present]

Rules:
- Only extract what is explicitly written in the resume.
- Do NOT add skills that are not mentioned.
- If information is missing, write "Not mentioned".
"""
)

# ─── STEP 2: Job Requirement Extraction ──────────────────────────────────────
JD_EXTRACTION_PROMPT = PromptTemplate(
    input_variables=["job_description"],
    template="""You are an expert recruiter analyzing a job description.
Extract the key requirements from the job description below.

Job Description:
{job_description}

Return in this exact format:

REQUIRED_SKILLS: [comma-separated list of required technical skills]
REQUIRED_EXPERIENCE_YEARS: [minimum years required as a number]
REQUIRED_TOOLS: [comma-separated list of required tools/frameworks]
PREFERRED_SKILLS: [nice-to-have skills, comma-separated]
"""
)

# ─── STEP 3: Matching ─────────────────────────────────────────────────────────
MATCHING_PROMPT = PromptTemplate(
    input_variables=["candidate_profile", "job_requirements"],
    template="""You are a hiring algorithm that compares a candidate profile to job requirements.

Candidate Profile:
{candidate_profile}

Job Requirements:
{job_requirements}

Perform a detailed match analysis and return in this exact format:

MATCHED_SKILLS: [skills present in both candidate profile and job requirements]
MISSING_SKILLS: [required skills NOT found in candidate profile]
MATCHED_TOOLS: [tools present in both candidate profile and job requirements]
MISSING_TOOLS: [required tools NOT found in candidate profile]
EXPERIENCE_MATCH: [Met / Partially Met / Not Met] – [brief reason]
OVERALL_MATCH_QUALITY: [Strong / Average / Weak]
"""
)

# ─── STEP 4: Scoring ──────────────────────────────────────────────────────────
SCORING_PROMPT = PromptTemplate(
    input_variables=["match_analysis", "job_requirements"],
    template="""You are a scoring engine for resume evaluation.
Based on the match analysis below, assign a score from 0 to 100.

Match Analysis:
{match_analysis}

Job Requirements (for reference):
{job_requirements}

Scoring Criteria (use these weights):
- Required Skills Coverage: 35 points
- Experience Match: 25 points
- Tools/Tech Stack Match: 20 points
- Education & Achievements: 10 points
- Preferred/Bonus Skills: 10 points

Return in this exact format:

SKILLS_SCORE: [0-35]
EXPERIENCE_SCORE: [0-25]
TOOLS_SCORE: [0-20]
EDUCATION_SCORE: [0-10]
BONUS_SCORE: [0-10]
TOTAL_SCORE: [0-100]
GRADE: [A (80-100) / B (60-79) / C (40-59) / D (below 40)]
"""
)

# ─── STEP 5: Explanation (with few-shot examples) ────────────────────────────
EXPLANATION_PROMPT = PromptTemplate(
    input_variables=["candidate_name", "total_score", "grade", "match_analysis", "scoring_details"],
    template="""You are an AI recruiter assistant generating a clear, honest hiring report.

Below are two examples of how to write explanations:

---
EXAMPLE 1:
Candidate: Jane Doe | Score: 85/100 | Grade: A
Explanation:
Jane is a strong fit for this role. She demonstrates deep expertise in Python, Scikit-learn, 
and TensorFlow, covering most required skills. Her 5 years of experience exceeds the 3-year 
requirement. She is missing Spark experience but compensates with strong MLOps and cloud skills. 
RECOMMENDATION: Proceed to technical interview.
---

EXAMPLE 2:
Candidate: John Smith | Score: 35/100 | Grade: D
Explanation:
John lacks most of the core technical requirements for this Data Scientist role. No ML or Python 
experience is evident in his resume. His background is primarily non-technical. 
RECOMMENDATION: Do not proceed at this time. Consider entry-level opportunities.
---

Now write an explanation for:

Candidate Name: {candidate_name}
Score: {total_score}/100
Grade: {grade}
Match Analysis: {match_analysis}
Scoring Details: {scoring_details}

Write a professional 3-5 sentence explanation covering:
1. Overall assessment
2. Key strengths
3. Key gaps
4. Final hiring recommendation

Format:
EXPLANATION: [your explanation here]
RECOMMENDATION: [Proceed to Interview / Hold for Review / Do Not Proceed]
HIRING_DECISION_CONFIDENCE: [High / Medium / Low]
"""
)
