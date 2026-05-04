import streamlit as st
import requests

# Update after Render deployment
API_URL = "https://resume-verifier.streamlit.app/analyze-resume"

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# Header
st.markdown("""
# 📄 AI Resume Analyzer
### Upload your resume and get AI-powered insights
""")

# Sidebar
with st.sidebar:
    st.header("Features")
    st.write("✅ Key Skills")
    st.write("✅ Missing Skills")
    st.write("✅ Suggested Job Roles")
    st.write("✅ Resume Improvements")

# File uploader
uploaded_file = st.file_uploader(
    "Upload Resume (PDF or DOCX)",
    type=["pdf", "docx"]
)

if uploaded_file:

    st.success("Resume uploaded successfully")

    col1, col2 = st.columns([3, 1])

    with col1:
        st.info(f"File: {uploaded_file.name}")

    with col2:
        analyze_button = st.button("Analyze 🚀")

    if analyze_button:

        with st.spinner("Analyzing resume..."):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    uploaded_file.type
                )
            }

            try:
                response = requests.post(
                    API_URL,
                    files=files
                )

                if response.status_code == 200:

                    result = response.json()

                    st.success("Analysis completed")

                    st.subheader("📊 Resume Analysis")
                    st.write(result["analysis"])

                    st.download_button(
                        label="Download Report",
                        data=result["analysis"],
                        file_name="resume_analysis.txt",
                        mime="text/plain"
                    )

                else:
                    st.error("Failed to analyze resume")
                    st.text(response.text)

            except Exception as e:
                st.error(f"Request failed: {e}")