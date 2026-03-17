SKILLS = [
    "python", "java", "sql", "machine learning",
    "react", "node", "aws", "docker",
    "data analysis", "pandas", "numpy"
]

def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    return found_skills