import re
from resume_parser import SKILL_DATABASE

REQUIRED_KEYWORDS = [
    "required",
    "requirements",
    "must have",
    "must-have",
    "essential",
    "mandatory"
]

PREFERRED_KEYWORDS = [
    "preferred",
    "nice to have",
    "nice-to-have",
    "bonus",
    "plus",
    "desirable",
    "optional"
]

def skill_exists(text, skill):
    pattern = r"(?<!\w)" + re.escape(skill.lower()) + r"(?!\w)"
    return re.search(pattern, text.lower()) is not None

def extract_skills_from_text(text):
    found_skills = []

    for skill in SKILL_DATABASE:
        if skill_exists(text, skill):
            found_skills.append(skill)

    return sorted(set(found_skills))

def find_section(job_description, keywords):
    lines = job_description.lower().splitlines()
    section_text = []
    capturing = False

    for line in lines:
        if any(keyword in line for keyword in keywords):
            capturing = True
            continue

        if capturing:
            if line.strip() == "":
                continue
            section_text.append(line)

    return "\n".join(section_text)

def parse_job_description(job_description):
    preferred_section = find_section(
        job_description,
        PREFERRED_KEYWORDS
    )

    preferred_skills = (
        extract_skills_from_text(preferred_section)
        if preferred_section
        else []
    )

    required_section = find_section(
        job_description,
        REQUIRED_KEYWORDS
    )

    required_skills = (
        extract_skills_from_text(required_section)
        if required_section
        else []
    )

    if not required_skills and not preferred_skills:
        required_skills = extract_skills_from_text(
            job_description
        )

    required_skills = [
        skill
        for skill in required_skills
        if skill not in preferred_skills
    ]

    return {
        "required_skills": required_skills,
        "preferred_skills": preferred_skills
    }
