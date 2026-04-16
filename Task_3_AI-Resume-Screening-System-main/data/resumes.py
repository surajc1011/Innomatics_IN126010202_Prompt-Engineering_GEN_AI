# ─────────────────────────────────────────────────────────────────────────────
# data/resumes.py  –  Three sample resumes (Strong / Average / Weak)
# ─────────────────────────────────────────────────────────────────────────────

JOB_DESCRIPTION = """
Position: Data Scientist
Company: TechCorp Analytics

Required Skills:
- Python (Pandas, NumPy, Scikit-learn)
- Machine Learning (Supervised & Unsupervised)
- Deep Learning (TensorFlow or PyTorch)
- SQL and database management
- Data visualization (Matplotlib, Seaborn, Tableau)
- Statistical analysis and hypothesis testing
- Natural Language Processing (NLP)
- MLOps / Model deployment experience

Experience Required: 3+ years in a data science or related role

Nice to Have:
- Experience with cloud platforms (AWS/GCP/Azure)
- Knowledge of Spark / Big Data tools
- Published research or Kaggle competition experience
"""

RESUMES = {
    "strong": {
        "name": "Atharv Jadhav",
        "level": "Strong Candidate",
        "text": """
Name: Atharv Jadhav
Email: atharv.jadhav@email.com
LinkedIn: linkedin.com/in/atharvjadhav

SUMMARY
Senior Data Scientist with 5 years of experience building production ML systems.
Passionate about turning data into actionable insights.

EXPERIENCE
Senior Data Scientist – DataFlow Inc. (2021–Present)
- Built and deployed 10+ ML models using Scikit-learn, XGBoost, TensorFlow
- Reduced customer churn by 22% using a gradient boosting classifier
- Designed NLP pipeline for sentiment analysis on 2M+ reviews using BERT
- Deployed models on AWS SageMaker; set up CI/CD pipelines for MLOps
- Led a team of 3 junior data scientists

Data Scientist – Analytics Hub (2019–2021)
- Developed recommendation engine using collaborative filtering (Python, Pandas)
- Performed A/B testing and hypothesis testing for product experiments
- Created dashboards in Tableau and Matplotlib for C-suite reporting

SKILLS
- Languages: Python, SQL, R
- ML Libraries: Scikit-learn, XGBoost, TensorFlow, PyTorch, HuggingFace
- Data Tools: Pandas, NumPy, Spark, Hadoop
- Visualization: Matplotlib, Seaborn, Tableau
- Cloud: AWS (SageMaker, S3, Lambda), GCP basics
- Other: Docker, Git, MLflow, Airflow

EDUCATION
M.Sc. Data Science – IIT Bombay (2019)
B.Tech Computer Science – VIT University (2017)

ACHIEVEMENTS
- Kaggle Expert (top 5% in 3 competitions)
- Published paper on graph neural networks – IEEE 2022
"""
    },

    "average": {
        "name": "Rahul Mehta",
        "level": "Average Candidate",
        "text": """
Name: Rahul Mehta
Email: rahul.mehta@email.com

SUMMARY
Data Analyst with 2 years of experience looking to transition into data science.
Strong in SQL and Python; currently upskilling in machine learning.

EXPERIENCE
Data Analyst – RetailVision Pvt. Ltd. (2022–Present)
- Wrote complex SQL queries to extract and analyze sales data
- Built automated Excel/Python reports saving 5 hours per week
- Created basic visualizations using Matplotlib and Power BI

Intern – StartupAI (2021–2022)
- Cleaned and preprocessed datasets using Pandas and NumPy
- Assisted in training a basic logistic regression model
- Explored Scikit-learn documentation and ran experiments

SKILLS
- Languages: Python, SQL
- Libraries: Pandas, NumPy, Scikit-learn (basic), Matplotlib
- Tools: Excel, Power BI, Jupyter Notebook
- Concepts: Linear regression, logistic regression, data cleaning

EDUCATION
B.Sc. Statistics – University of Pune (2021)

COURSES / CERTIFICATIONS
- Coursera: Machine Learning by Andrew Ng (completed)
- Udemy: Python for Data Science (completed)
- Currently learning: TensorFlow basics
"""
    },

    "weak": {
        "name": "Anil Patil",
        "level": "Weak Candidate",
        "text": """
Name: Anil Patil
Email: anil.patil@email.com

OBJECTIVE
Fresher looking for an opportunity in the IT sector.
Willing to learn and work hard.

EXPERIENCE
None (fresher)

SKILLS
- Microsoft Office (Word, Excel, PowerPoint)
- Basic knowledge of C and C++
- Some exposure to HTML and CSS
- Familiar with the concept of databases

EDUCATION
B.Com – Savitribai Phule Pune University (2023)
10th & 12th – Maharashtra State Board

PROJECTS
- Made a website for a college event using HTML/CSS
- Created an Excel sheet to track monthly household expenses

HOBBIES
- Cricket, Reading, Travelling
"""
    }
}
