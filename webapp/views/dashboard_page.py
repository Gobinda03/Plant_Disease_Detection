import streamlit as st
import plotly.express as px

from src.history import get_reports
from src.dashboard import build_stats

def show_dashboard_page():

    st.title(
        "Community Dashboard"
    )

    reports = get_reports()

    stats = build_stats(reports)

    if not stats:

        st.info(
            "No data available."
        )

        return

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Total Reports",
            len(reports)
        )

    with col2:
        st.metric(
            "Unique Diseases",
            len(stats)
        )

    chart = px.bar(
        x=list(stats.keys()),
        y=list(stats.values()),
        title="Disease Frequency"
    )

    st.plotly_chart(
        chart,
        width="stretch"
    )