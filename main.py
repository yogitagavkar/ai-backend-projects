import streamlit as st
import requests
import json

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

API_URL = "https://ai-resume-analyzer.onrender.com/"

# Header
st.markdown("""
# 📄 AI Resume Analyzer
### Upload your resume and get instant AI-powered career insights
""")

# Sidebar
with st.sidebar:
    st.header("Features")
    st.write("✅ Key Skills Detection")
    st.write("✅ Missing Skills Analysis")
    st.write("✅ Suggested Job Roles")
    st.write("✅ Resume Improvement Suggestions")

# Upload Section
uploaded_file = st.file_uploader(
    "Upload Resume (PDF/DOCX)",
    type=["pdf", "docx"]
)

if uploaded_file:

    st.success("Resume uploaded successfully")

    col1, col2 = st.columns([2,1])

    with col1:
        st.info(f"File Name: {uploaded_file.name}")

    with col2:
        analyze_button = st.button("Analyze Resume 🚀")

    if analyze_button:

        with st.spinner("Analyzing resume..."):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    uploaded_file.type
                )
            }

            response = requests.post(
                API_URL,
                files=files
            )

            if response.status_code == 200:

                result = response.json()

                st.success("Analysis Completed")

                analysis_text = result["analysis"]

                tab1, tab2 = st.tabs([
                    "📌 Analysis",
                    "📥 Export"
                ])

                with tab1:
                    st.markdown("### AI Insights")
                    st.write(analysis_text)

                with tab2:
                    st.download_button(
                        label="Download Analysis",
                        data=analysis_text,
                        file_name="resume_analysis.txt",
                        mime="text/plain"
                    )

            else:
                st.error("Error analyzing resume")