import streamlit as st
from src.alerts import get_disease_alerts


def render_header():

    st.title(
        "🌿 AgriDoctor AI"
    )

    alerts = get_disease_alerts()

    for alert in alerts:

        st.warning(
            f"""
🚨 Community Disease Alert

Disease: {alert['disease']}

Location: {alert['district']}

Detected {alert['count']} times recently.
"""
        )