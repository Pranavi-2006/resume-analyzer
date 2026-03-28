def read_resume(file_path):
    """Reads resume content from file"""
    try:
        with open(file_path, "r") as file:
            return file.read().lower()
    except FileNotFoundError:
        print("Error: Resume file not found.")
        return ""


def analyze_skills(resume_text, keywords):
    """Find matching skills and calculate score"""
    found = []
    for skill in keywords:
        if skill in resume_text:
            found.append(skill)
    score = len(found)
    return found, score


def check_sections(resume_text, sections):
    """Check if important sections exist"""
    missing = []
    for section in sections:
        if section not in resume_text:
            missing.append(section)
    return missing


def generate_feedback(score, total_keywords, missing_sections):
    """Generate suggestions based on analysis"""
    feedback = []

    if score < total_keywords // 2:
        feedback.append("Add more relevant technical skills.")

    if missing_sections:
        feedback.append(f"Include sections: {', '.join(missing_sections)}")

    if not feedback:
        feedback.append("Your resume looks good!")

    return feedback


def main():
    print("=== AI Resume Analyzer ===\n")

    resume_text = read_resume("resume.txt")

    if not resume_text:
        return

    keywords = [
        "python", "java", "c", "sql",
        "machine learning", "communication", "teamwork"
    ]

    sections = ["education", "skills", "projects"]

    found_skills, score = analyze_skills(resume_text, keywords)
    missing_sections = check_sections(resume_text, sections)
    feedback = generate_feedback(score, len(keywords), missing_sections)

    # Output
    print("Skills Found:", found_skills)
    print(f"Score: {score}/{len(keywords)}")

    print("\nMissing Sections:", missing_sections if missing_sections else "None")

    print("\nSuggestions:")
    for tip in feedback:
        print("-", tip)


if __name__ == "__main__":
    main()