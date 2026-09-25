from matcher import calculate_similarity

def match_skills(
    resume_skills,
    required_skills,
    preferred_skills
):
    resume_set = {skill.lower() for skill in resume_skills}
    required_set = {skill.lower() for skill in required_skills}
    preferred_set = {skill.lower() for skill in preferred_skills}

    matched_required = sorted(
        resume_set.intersection(required_set)
    )

    missing_required = sorted(
        required_set.difference(resume_set)
    )

    matched_preferred = sorted(
        resume_set.intersection(preferred_set)
    )

    missing_preferred = sorted(
        preferred_set.difference(resume_set)
    )

    if len(required_set) > 0:
        required_score = (
            len(matched_required) / len(required_set)
        ) * 100
    else:
        required_score = 100

    if len(preferred_set) > 0:
        preferred_score = (
            len(matched_preferred) / len(preferred_set)
        ) * 100
    else:
        preferred_score = 100

    skill_score = (
        required_score * 0.80
        + preferred_score * 0.20
    )

    return {
        "matched_required": matched_required,
        "missing_required": missing_required,
        "matched_preferred": matched_preferred,
        "missing_preferred": missing_preferred,
        "required_skill_score": round(required_score, 2),
        "preferred_skill_score": round(preferred_score, 2),
        "skill_match_score": round(skill_score, 2)
    }

def analyze_match(
    resume_text,
    job_description,
    resume_skills,
    required_skills,
    preferred_skills
):
    skill_result = match_skills(
        resume_skills,
        required_skills,
        preferred_skills
    )

    text_similarity_score = calculate_similarity(
        resume_text,
        job_description
    )

    overall_score = (
        skill_result["skill_match_score"] * 0.60
        + text_similarity_score * 0.40
    )

    return {
        **skill_result,
        "text_similarity_score": text_similarity_score,
        "overall_score": round(overall_score, 2)
    }
