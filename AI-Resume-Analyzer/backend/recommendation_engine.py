SKILL_CATEGORIES = {
    "programming": [
        "python",
        "java",
        "javascript",
        "c",
        "c++"
    ],
    "web_development": [
        "html",
        "css",
        "javascript",
        "react",
        "node.js",
        "fastapi",
        "flask",
        "django"
    ],
    "data_ai": [
        "machine learning",
        "deep learning",
        "tensorflow",
        "pytorch",
        "scikit-learn",
        "pandas",
        "numpy",
        "opencv",
        "data analysis"
    ],
    "databases": [
        "mysql",
        "postgresql",
        "mongodb"
    ],
    "devops": [
        "git",
        "github",
        "docker",
        "aws"
    ]
}

def categorize_skill(skill):
    skill_lower = skill.lower()

    for category, skills in SKILL_CATEGORIES.items():
        if skill_lower in skills:
            return category

    return "other"

def generate_recommendations(missing_skills):
    recommendations = []

    for skill in missing_skills:
        category = categorize_skill(skill)

        if category == "programming":
            message = f"Learn the fundamentals of {skill}."
        elif category == "web_development":
            message = (
                f"Practice building a small web project using {skill}."
            )
        elif category == "data_ai":
            message = (
                f"Study {skill} and build a small practical project."
            )
        elif category == "databases":
            message = (
                f"Learn {skill} basics and practice database queries."
            )
        elif category == "devops":
            message = (
                f"Learn the fundamentals of {skill} "
                "and use it in a project."
            )
        else:
            message = (
                f"Research {skill} and practice it with a small project."
            )

        recommendations.append({
            "skill": skill,
            "category": category,
            "recommendation": message
        })

    return recommendations
