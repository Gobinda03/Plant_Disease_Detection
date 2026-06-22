from datetime import datetime, timedelta
from src.database import supabase
from src.logger import log_event

from src.auth import get_user
from src.profile import get_profile

WARNING_THRESHOLD = 5
HIGH_RISK_THRESHOLD = 15
OUTBREAK_THRESHOLD = 30


def get_disease_alerts():
    user = get_user()

    profile = get_profile(
        user.user.id
    )
    district = profile["district"]
    seven_days_ago = (
        datetime.utcnow()
        - timedelta(days=7)
    ).isoformat()
    reports = (
        supabase
        .table("disease_reports")
        .select("*")
        .gte(
            "created_at",
            seven_days_ago
        )
        .eq(
            "district",
            district
        )
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

        if count >= OUTBREAK_THRESHOLD:

            level = "OUTBREAK"

            alerts.append(
                {
                    "district": district,
                    "disease": disease,
                    "count": count,
                    "level": level
                }
            )

            log_event(
                f"ALERT: {disease}",
                {
                    "district": district,
                    "cases": count
                }
            )
        elif count >= HIGH_RISK_THRESHOLD:

            level = "HIGH RISK"
            alerts.append(
                {
                    "district": district,
                    "disease": disease,
                    "count": count,
                    "level": level
                }
            )

            log_event(
                f"ALERT: {disease}",
                {
                    "district": district,
                    "cases": count
                }
            )
        elif count >= WARNING_THRESHOLD:

            level = "WARNING"

            alerts.append(
                {
                    "district": district,
                    "disease": disease,
                    "count": count,
                    "level": level
                }
            )

            log_event(
                f"ALERT: {disease}",
                {
                    "district": district,
                    "cases": count
                }
            )
        else:
            continue

    return alerts