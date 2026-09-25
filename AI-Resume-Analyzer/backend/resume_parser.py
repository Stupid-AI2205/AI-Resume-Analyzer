import re

SKILL_DATABASE = [
    "python",
    "java",
    "javascript",
    "c++",
    "c",
    "sql",
    "html",
    "css",
    "react",
    "node.js",
    "fastapi",
    "flask",
    "django",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
    "scikit-learn",
    "opencv",
    "git",
    "github",
    "docker",
    "aws",
    "mongodb",
    "postgresql",
    "mysql",
    "data analysis",
    "pandas",
    "numpy"
]

SECTION_NAMES = [
    "education",
    "experience",
    "work experience",
    "projects",
    "certifications",
    "certificates",
    "skills"
]

def extract_email(text):
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    match = re.search(pattern, text)
    return match.group() if match else None

def extract_phone(text):
    pattern = r"(?:\+91[\s-]?)?[6-9]\d{9}"
    match = re.search(pattern, text)
    return match.group() if match else None

def extract_skills(text):
    text_lower = text.lower()
    found_skills = []

    for skill in SKILL_DATABASE:
        skill_lower = skill.lower()
        pattern = r"(?<!\w)" + re.escape(skill_lower) + r"(?!\w)"

        if re.search(pattern, text_lower):
            found_skills.append(skill)

    if re.search(r"(?<!\w)ml(?!\w)", text_lower):
        if "machine learning" not in found_skills:
            found_skills.append("machine learning")

    if re.search(r"(?<!\w)ai(?!\w)", text_lower):
        found_skills.append("artificial intelligence")

    return sorted(set(found_skills))

def extract_sections(text):
    lines = text.splitlines()
    sections = {}
    current_section = None

    for line in lines:
        clean_line = line.strip()
        if not clean_line:
            continue

        lower_line = clean_line.lower()
        detected_section = None

        for section in SECTION_NAMES:
            if lower_line == section:
                detected_section = section
                break

        if detected_section:
            current_section = detected_section
            if current_section not in sections:
                sections[current_section] = []
            continue

        if current_section:
            sections[current_section].append(clean_line)

    return sections

def parse_resume(text):
    sections = extract_sections(text)

    return {
        "contact": {
            "email": extract_email(text),
            "phone": extract_phone(text)
        },
        "skills": extract_skills(text),
        "education": sections.get("education", []),
        "experience": sections.get(
            "experience",
            sections.get("work experience", [])
        ),
        "projects": sections.get("projects", []),
        "certifications": sections.get(
            "certifications",
            sections.get("certificates", [])
        )
    }
