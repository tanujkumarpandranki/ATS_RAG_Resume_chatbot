from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")


def compute_similarity(resume, job):

    emb = model.encode([resume, job])

    score = cosine_similarity(
        [emb[0]], [emb[1]]
    )[0][0] * 100

    return round(score, 2)


def compute_ats(similarity, resume_skills, job_skills):

    if len(job_skills) > 0:
        skill_score = (len(set(resume_skills) & set(job_skills)) / len(job_skills)) * 100
    else:
        skill_score = 0

    ats = (0.6 * similarity) + (0.4 * skill_score)

    return round(ats, 2)