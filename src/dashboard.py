from collections import Counter

def build_stats(data):

    diseases = [
        row["disease_name"]
        for row in data
    ]

    return Counter(diseases)