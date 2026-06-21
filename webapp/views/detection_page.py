import streamlit as st
from PIL import Image
import tempfile

from src.predict import predict_disease
from src.knowledge_base import get_disease_info
from src.reports import save_report

try:
    from src.llm_report import generate_report
    LLM_AVAILABLE = True
except Exception:
    LLM_AVAILABLE = False


def show_detection_page():

    
    # ---------- Hero Section ---------- 

    st.title("🌿 Plant Disease Detection")

    st.markdown("""
    ### Detect Plant Diseases Instantly

    Upload a plant leaf image and receive:

    ✅ Disease Prediction  
    ✅ Confidence Score  
    ✅ Symptoms Analysis  
    ✅ Organic Treatments  
    ✅ AI Generated Report  
    ✅ Community Disease Alerts
    """)

    st.caption(
        "Supported Crops: Apple • Corn • Grape • Potato • Tomato"
    )

    st.divider()

    
    # ---------- Feature Cards ---------- 

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("🔍 Disease Detection")

    with col2:
        st.info("🤖 AI Reports")

    with col3:
        st.info("📍 Community Alerts")

    st.divider()

   
    # ---------- Upload Image ---------- 

    uploaded_file = st.file_uploader(
        "📤 Upload Leaf Image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is None:
        return

    image = Image.open(uploaded_file)

    col1, col2 = st.columns([1, 1])

    
    # ---------- Display Image ---------- 

    with col1:

        st.image(
            image,
            caption="Uploaded Leaf",
            width="stretch"
        )

    
    # ---------- Prediction ---------- 

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".jpg"
    ) as tmp:

        image.save(tmp.name)

        disease_name, confidence = predict_disease(
            tmp.name
        )

    with col2:

        st.success("✅ Prediction Complete")

        st.metric(
            "Detected Disease",
            disease_name.replace("_", " ")
        )

        st.metric(
            "Confidence",
            f"{confidence:.2f}%"
        )

        if confidence >= 90:

            st.success(
                "High Confidence Prediction"
            )

        elif confidence >= 70:

            st.warning(
                "Moderate Confidence Prediction"
            )

        else:

            st.error(
                "Low Confidence Prediction"
            )

        st.progress(
            min(
                int(confidence),
                100
            )
        )


    # ---------- Disease Information ---------- 

    try:

        disease_info = get_disease_info(
            disease_name
        )

        st.divider()

        st.header(
            "📚 Disease Information"
        )

        st.write(
            disease_info.get(
                "description",
                "Information unavailable."
            )
        )

        with st.expander(
            "🦠 Symptoms"
        ):

            symptoms = disease_info.get(
                "symptoms",
                []
            )

            for symptom in symptoms:

                st.write(
                    f"• {symptom}"
                )

        with st.expander(
            "🌱 Organic Treatment Recommendations"
        ):

            treatments = disease_info.get(
                "organic_treatment",
                []
            )

            for treatment in treatments:

                st.write(
                    f"• {treatment}"
                )

    except Exception as e:

        st.warning(
            f"Disease information unavailable: {e}"
        )


    # ---------- AI Report ---------- 

    st.divider()

    st.header(
        "🤖 AI Disease Report"
    )

    if not LLM_AVAILABLE:

        st.warning(
            "LLM service is unavailable."
        )

        return

    if st.button(
        "Generate AI Report",
        width="stretch"
    ):

        with st.spinner(
            "Generating AI report..."
        ):

            try:

                report = generate_report(
                    disease_name,
                    confidence
                )

                save_report(
                    disease_name,
                    confidence,
                    report
                )

                st.success(
                    "Report saved successfully."
                )

                st.markdown(
                    report
                )

            except Exception as e:

                st.error(
                    f"Report generation failed: {e}"
                )
