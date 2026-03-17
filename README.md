# AI-Resume-Ranking-and-Parsing-System
# AI Resume Ranking & Parsing System

## Overview

This project is an AI-powered Resume Ranking System that automatically analyzes and ranks multiple resumes based on a given Job Description (JD). It simulates a real-world recruitment scenario where candidates are evaluated based on their skills, experience, education, and location.

---

## Features

* Upload multiple resumes (PDF/DOCX)
* Extract candidate details (Name, Email, Phone, Experience)
* Identify technical skills from resumes
* Compare resumes with Job Description
* Rank candidates based on scoring algorithm
* Display results in a clean dashboard

---

## Tech Stack

* Python
* Streamlit (for UI)
* pdfplumber (for PDF parsing)
* python-docx (for DOCX parsing)
* Regular Expressions (for data extraction)
* Pandas (for dashboard table)

---

## ⚙️ Setup Instructions

1. Clone the repository:

```
git clone <your-repo-link>
cd resume_ranker
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the application:

```
streamlit run app.py
```

---

## How It Works

### 1. Resume Parsing

* Extracts text from PDF and DOCX files
* Identifies key details like name, email, phone, and experience

### 2. Skill Extraction

* Matches predefined technical skills (Python, Java, SQL, etc.)
* Uses keyword-based extraction

### 3. Job Description Matching

* Compares extracted skills with JD
* Performs partial matching for better accuracy

### 4. Candidate Ranking Algorithm

Candidates are scored based on the following weighted factors:
<img width="608" height="157" alt="image" src="https://github.com/user-attachments/assets/d34beef6-8351-4752-bffe-24d13d0cfabf" />

#### Scoring Logic:

* **Skills Score (50%)**: Based on how many skills match the JD
* **Experience Score (25%)**:

  * ≥ 3 years → High score
  * 2 years → Medium score
  * < 2 years → Low score
* **Education Score (10%)**:

  * B.Tech / B.E → Full score
  * Others → Partial score
* **Location Score (15%)**:

  * Matches preferred region → Full score

Final Score = Sum of all above factors

---

## Output Dashboard

The system displays ranked candidates in the following format:

<img width="886" height="33" alt="image" src="https://github.com/user-attachments/assets/594078ad-f4f9-420d-a4e7-fc38292ff3f2" />

Candidates are sorted in descending order of score.

---

## Demo



---

## Notes

* This project focuses on logic and problem-solving rather than production-level optimization.
* No external APIs were used, as per assignment requirements.

---

## 🙌 Conclusion

This system demonstrates how AI and NLP techniques can be applied to automate resume screening and candidate ranking efficiently.

---
