import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))



import streamlit as st

from webapp.views.auth_page import show_auth_page
from webapp.views.detection_page import show_detection_page
from webapp.views.history_page import show_history_page
from webapp.views.dashboard_page import show_dashboard_page

from webapp.components.header import render_header

from src.auth import get_user, sign_out


#---------- Page Config ----------

st.set_page_config(
    page_title="AgriDoctor AI",
    page_icon="🌿",
    layout="wide"
)

#---------- Authentication Check ----------

try:
    current_user = get_user()

    authenticated = (
        current_user is not None
        and current_user.user is not None
    )

except Exception:
    authenticated = False
    current_user = None


#---------- Login Page ----------

if not authenticated:
    show_auth_page()
    st.stop()


#---------- Sidebar ----------

st.sidebar.success(
    f"Logged in as\n\n{current_user.user.email}"
)

page = st.sidebar.selectbox(
    "Navigation",
    [
        "Disease Detection",
        "My Reports",
        "Dashboard"
    ]
)

if st.sidebar.button("Logout"):
    sign_out()
    st.rerun()


#---------- Header ----------

render_header()


#---------- Routing ----------

if page == "Disease Detection":
    show_detection_page()

elif page == "My Reports":
    show_history_page()

elif page == "Dashboard":
    show_dashboard_page()