import streamlit as st
from streamlit_geolocation import streamlit_geolocation

from src.auth import sign_up, sign_in
from src.profile import create_profile
from src.geocoding import get_address
from src.location_data import INDIA_LOCATIONS

from src.logger import log_event

def show_auth_page():


    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        st.title("🌿 AgriDoctor AI")
        st.caption(
            "AI-powered Plant Disease Detection & Community Alerts"
        )

        tab1, tab2 = st.tabs(
            ["Login", "Register"]
        )

        # ---------- LOGIN ----------

        with tab1:

            st.subheader("Welcome Back")

            email = st.text_input(
                "Email",
                key="login_email"
            )

            password = st.text_input(
                "Password",
                type="password",
                key="login_password"
            )

            if st.button(
                "Login",
                width="stretch"
            ):

                try:

                    log_event(
                        "LOGIN ATTEMPT",
                        {
                            "email": email
                        }
                    )

                    sign_in(
                        email,
                        password
                    )

                    st.success(
                        "Login successful"
                    )
                    log_event(
                        "LOGIN SUCCESS",
                        {
                            "email": email
                        }
                    )

                    st.rerun()

                except Exception as e:
                    log_event(
                        "LOGIN FAILED",
                        {
                            "email": email,
                            "error": str(e)
                        }
                    )
                    st.error(str(e))

        # ---------- REGISTER ----------

        with tab2:

            st.subheader(
                "Create Account"
            )

            email = st.text_input(
                "Email Address",
                key="register_email"
            )

            password = st.text_input(
                "Password",
                type="password",
                key="register_password"
            )

            st.markdown("### 📍 Location")

            st.caption(
                "Allow location access to receive disease alerts near you."
            )

            location = streamlit_geolocation()

            latitude = None
            longitude = None

            selected_state = None
            selected_district = None

            if (
                location
                and location.get("latitude") is not None
            ):

                latitude = location["latitude"]
                longitude = location["longitude"]

                address = get_address(
                    latitude,
                    longitude
                )

                detected_state = address.get(
                    "state",
                    "Unknown"
                )

                detected_district = address.get(
                    "district",
                    "Unknown"
                )

                st.success(
                    "Location Detected"
                )
                log_event(
                    "LOCATION DETECTED",
                    {
                        "district": detected_district,
                        "state": detected_state,
                        "latitude": latitude,
                        "longitude": longitude
                    }
                )

                st.info(
                    f"""
                    📍 District: {detected_district}
                    📍 State: {detected_state}
                    """
                )


                location_correct = st.checkbox(
                    "Location is correct",
                    value=True
                )

                if not location_correct:

                    st.warning(
                        "Please choose your correct location."
                    )

                    states = list(
                        INDIA_LOCATIONS.keys()
                    )

                    selected_state = st.selectbox(
                        "State",
                        states
                    )

                    selected_district = st.selectbox(
                        "District",
                        INDIA_LOCATIONS[
                            selected_state
                        ]
                    )

                    log_event(
                        "LOCATION ENTERED",
                        {
                            "district": selected_district,
                            "state": selected_state
                        }
                    )

                else:

                    selected_state = detected_state
                    selected_district = detected_district

            else:

                st.info(
                    "Please allow location access."
                )

            if st.button(
                "Create Account",
                width="stretch"
            ):

                try:

                    if latitude is None:

                        st.error(
                            "Location permission is required."
                        )

                    else:
                        log_event(
                            "SIGNUP ATTEMPT",
                            {
                                "email": email
                            }
                        )

                        response = sign_up(
                            email,
                            password
                        )

                        create_profile(
                            user_id=response.user.id,
                            email=email,
                            state=selected_state,
                            district=selected_district,
                            latitude=latitude,
                            longitude=longitude
                        )

                        st.success(
                            "Account created successfully!"
                        )
                        log_event(
                            "PROFILE CREATED",
                            {
                                "email": email,
                                "district": selected_district,
                                "state": selected_state
                            }
                        )

                        log_event(
                            "SIGNUP SUCCESS",
                            {
                                "email": email,
                                "user_id": response.user.id
                            }
                        )

                        st.info(
                            "You can now log in."
                        )

                except Exception as e:
                    log_event(
                        "SIGNUP FAILED",
                        {
                            "email": email,
                            "error": str(e)
                        }
                    )
                    st.error(str(e))

