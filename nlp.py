import json
import re   

with open("skills.json") as f:
    skills_data = json.load(f)

all_skills = []

for category in skills_data.values():
    all_skills.extend(category)

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text


def extract_skills(text):
    text = text.lower()
    found = []

    for skill in all_skills:
        if skill in text:
            found.append(skill)

    return list(set(found))

def categorize_skills(found_skills):
    result = {}

    for category, skills in skills_data.items():
        matched = list(set(found_skills) & set(skills))
        if matched:
            result[category] = matched

    return result