import json

with open(
    "dataset/disease_knowledge.json",
    "r"
) as f:
    disease_db = json.load(f)

def get_disease_info(disease):
    return disease_db.get(disease)