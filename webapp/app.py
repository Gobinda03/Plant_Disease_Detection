import sys
from pathlib import Path

# ==================================
# Add project root to Python path
# ==================================

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

# ==================================
# Imports
# ==================================

import streamlit as st
from PIL import Image
import tempfile

from src.predict import predict_disease
from src.knowledge_base import get_disease_info


try:
    from src.llm_report import generate_report
    LLM_AVAILABLE = True

except Exception as e:
    LLM_AVAILABLE = False
    st.error(f"LLM Import Error: {e}")

# ==================================
# Page Config
# ==================================

st.set_page_config(
    page_title="Plant Disease Detection",
    page_icon="🌿",
    layout="wide"
)

# ==================================
# Header
# ==================================

st.title("🌿 Plant Disease Detection System")

st.markdown("""
Upload a plant leaf image and get:

- Disease Detection
- Confidence Score
- Disease Information
- Organic Treatment Recommendation
- AI Generated Report
""")

# ==================================
# Upload Image
# ==================================

uploaded_file = st.file_uploader(
    "Upload Leaf Image",
    type=["jpg", "jpeg", "png"]
)

# ==================================
# Prediction
# ==================================

if uploaded_file:

    image = Image.open(uploaded_file)

    col1, col2 = st.columns([1, 1])

    with col1:

        st.image(
            image,
            caption="Uploaded Image",
            use_container_width=True
        )

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".jpg"
    ) as tmp:

        image.save(tmp.name)

        disease_name, confidence = predict_disease(
            tmp.name
        )

    with col2:

        st.success("Prediction Complete")

        st.subheader("Detected Disease")

        st.write(disease_name)

        st.subheader("Confidence")

        st.progress(
            min(int(confidence), 100)
        )

        st.write(f"{confidence:.2f}%")

    # ==================================
    # Disease Information
    # ==================================

    try:

        disease_info = get_disease_info(
            disease_name
        )

        st.divider()

        st.header("Disease Information")

        st.write(
            disease_info.get(
                "description",
                "Information unavailable."
            )
        )

        st.subheader("Symptoms")

        symptoms = disease_info.get(
            "symptoms",
            []
        )

        for item in symptoms:
            st.write(f"• {item}")

        st.subheader(
            "Organic Treatment Recommendation"
        )

        treatments = disease_info.get(
            "organic_treatment",
            []
        )

        for item in treatments:
            st.write(f"• {item}")

    except Exception as e:

        st.warning(
            f"Disease information unavailable: {e}"
        )

    # ==================================
    # LLM Report
    # ==================================

    # if LLM_AVAILABLE:

    st.divider()

    st.header(
        "AI Generated Disease Report"
    )

    if st.button(
        "Generate AI Report"
    ):

        with st.spinner(
            "Generating report..."
        ):

            try:

                report = generate_report(
                    disease_name,
                    confidence
                )

                st.markdown(report)

            except Exception as e:

                st.error(
                    f"Report generation failed: {e}"
                )