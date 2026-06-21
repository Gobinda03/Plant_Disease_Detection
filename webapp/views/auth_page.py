import streamlit as st
from streamlit_geolocation import streamlit_geolocation

from src.auth import sign_up, sign_in
from src.profile import create_profile
from src.geocoding import get_address


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
                use_container_width=True
            ):

                try:

                    sign_in(
                        email,
                        password
                    )

                    st.success(
                        "Login successful"
                    )

                    st.rerun()

                except Exception as e:

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

            location_ready = (
                location
                and location.get("latitude")
                is not None
            )

            if location_ready:

                st.success(
                    "Location captured successfully"
                )

            else:

                st.info(
                    "Please allow location access."
                )

            if st.button(
                "Create Account",
                use_container_width=True
            ):

                try:

                    if not location_ready:

                        st.error(
                            "Location permission is required."
                        )

                    else:

                        response = sign_up(
                            email,
                            password
                        )

                        latitude = location[
                            "latitude"
                        ]

                        longitude = location[
                            "longitude"
                        ]

                        address = get_address(
                            latitude,
                            longitude
                        )

                        create_profile(
                            user_id=response.user.id,
                            email=email,
                            state=address["state"],
                            district=address["district"],
                            latitude=latitude,
                            longitude=longitude
                        )

                        st.success(
                            "Account created successfully!"
                        )

                        st.info(
                            "You can now log in."
                        )

                except Exception as e:

                    st.error(str(e))