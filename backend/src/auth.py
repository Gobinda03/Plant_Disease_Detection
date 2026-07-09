import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv
from supabase import create_client

from backend.src.logger import log_event

ROOT_DIR = Path(__file__).resolve().parents[2]
load_dotenv(ROOT_DIR / ".env")

try:
    SUPABASE_URL = st.secrets["SUPABASE_URL"]
    SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
except Exception:
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY,
)

#---------- Sign Up ----------

def sign_up(email, password):

    try:

        response = supabase.auth.sign_up(
            {
                "email": email,
                "password": password
            }
        )

        log_event(
            "SIGNUP SUCCESS",
            {
                "email": email,
                "user_id": response.user.id
            }
        )

        return response

    except Exception as e:

        log_event(
            "SIGNUP FAILED",
            {
                "email": email,
                "error": str(e)
            }
        )

        raise e



#---------- Sign In ----------

def sign_in(email, password):

    log_event(
        "LOGIN ATTEMPT",
        {
            "email": email
        }
    )

    try:

        response = supabase.auth.sign_in_with_password(
            {
                "email": email,
                "password": password
            }
        )

        log_event(
            "LOGIN SUCCESS",
            {
                "email": email,
                "user_id": response.user.id
            }
        )

        return response

    except Exception as e:

        log_event(
            "LOGIN FAILED",
            {
                "email": email,
                "error": str(e)
            }
        )

        raise e

#---------- Sign Out ----------

def sign_out():

    try:

        user = get_user()

        if user and user.user:

            log_event(
                "USER LOGOUT",
                {
                    "email": user.user.email
                }
            )

        supabase.auth.sign_out()

    except Exception as e:

        log_event(
            "LOGOUT FAILED",
            {
                "error": str(e)
            }
        )

        raise e


#---------- Current User ----------

def get_user():

    try:

        return supabase.auth.get_user()

    except Exception as e:

        log_event(
            "GET USER FAILED",
            {
                "error": str(e)
            }
        )

        return None