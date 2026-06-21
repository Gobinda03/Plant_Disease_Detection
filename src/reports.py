from src.database import supabase
from src.auth import get_user
from datetime import datetime, timezone
from src.profile import get_profile
from src.logger import log_event


def save_report(disease_name, confidence, report):
    user = get_user()
    user_id = user.user.id
    profile = get_profile(user_id)
    data = {
        "user_id": user_id,
        "disease_name": disease_name,
        "confidence": confidence,
        "report": report,
        "state": profile["state"],
        "district": profile["district"],
        "latitude": profile["latitude"],
        "longitude": profile["longitude"],
        "created_at": datetime.now(timezone.utc).isoformat()
    }
    response = supabase.table(
        "disease_reports"
    ).insert(
        data
    ).execute()

    log_event(
        "REPORT GENERATED",
        {
            "disease": disease_name
        }
    )
    return response