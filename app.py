import pandas as pd
from info_extractor import extract_contact_info, extract_name, extract_experience
from info_extractor import extract_contact_info
from skills import extract_skills
from parser import extract_text
import streamlit as st

st.title("AI Resume Ranking System")

jd = st.text_area("Enter Job Description 👇")

st.write("Upload resumes below 👇")

# Upload multiple files
uploaded_files = st.file_uploader(
    "Upload Resumes (PDF/DOCX)",
    type=["pdf", "docx"],
    accept_multiple_files=True
)

# Show uploaded file names
results = []

if uploaded_files and jd:
    st.write("### Ranked Candidates:")

    for file in uploaded_files:
        text = extract_text(file)
        skills = extract_skills(text)
        contact = extract_contact_info(text)
        name = extract_name(text)
        experience = extract_experience(text)

        jd_lower = jd.lower()

        matched = []
        for skill in skills:
            skill_words = skill.lower().split()
            for word in skill_words:
                if word in jd_lower:
                    matched.append(skill)
                    break

        # 🎯 SCORING LOGIC
        # 🎯 SKILL SCORE (50)
        if len(skills) > 0:
            skill_score = (len(matched) / len(skills)) * 50
        else:
            skill_score = 0
        # 🎯 EXPERIENCE SCORE (25)
        exp_score = 0
        if "year" in experience.lower():
            try:
                exp_value = int(experience.split()[0])
                if exp_value >= 3:
                    exp_score = 25
                elif exp_value == 2:
                    exp_score = 15
                else:
                    exp_score = 5
            except:
                exp_score = 5
        # 🎯 EDUCATION SCORE (10)
        education_score = 10 if "btech" in text.lower() or "b.e" in text.lower() else 5
        
        # 🎯 LOCATION SCORE (15)
        location_score = 15 if "india" in text.lower() else 5
        
        # ✅ FINAL SCORE
        score = skill_score + exp_score + education_score + location_score
        

        results.append({
            "name": name,
            "skills": skills,
            "matched": matched,
            "score":round(score, 2),
            "email": contact["email"],
            "phone": contact["phone"],
            "experience": experience
        })

    # 🔥 SORT (highest score first)
    results = sorted(results, key=lambda x: x["score"], reverse=True)

    # 🎉 DISPLAY RANKING
    data = []
    for i, r in enumerate(results):
        data.append({
            "Rank": i + 1,
            "Name": r["name"],
            "Skills": ", ".join(r["skills"]),
            "Experience": r["experience"],
            "Score": r["score"]
        })
    df = pd.DataFrame(data)
    
    st.write("### 📊 Candidate Ranking Dashboard")
    st.dataframe(df, use_container_width=True, hide_index=True)
