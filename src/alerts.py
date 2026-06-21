from src.database import supabase
from src.logger import log_event

THRESHOLD = 5


def get_disease_alerts():

    reports = (
        supabase
        .table("disease_reports")
        .select("*")
        .execute()
        .data
    )

    counts = {}

    for report in reports:

        key = (
            report["district"],
            report["disease_name"]
        )

        counts[key] = (
            counts.get(key, 0) + 1
        )

    alerts = []

    for (
        district,
        disease
    ), count in counts.items():

        if count >= THRESHOLD:

            alerts.append(
                {
                    "district": district,
                    "disease": disease,
                    "count": count
                }
            )
            log_event(
                f"ALERT: {disease}",
                {
                    "district": district,
                    "cases": count
                }
            )

    return alerts