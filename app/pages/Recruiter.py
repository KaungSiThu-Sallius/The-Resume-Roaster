import sys
import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Add the project root to the python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.utils import extract_text_from_upload, calculate_similarity

st.set_page_config(page_title="Resume Roaster", page_icon="📄")

if "resume_input" not in st.session_state:
    st.session_state['resume_input'] = 0

def clear_form():
    st.session_state["jd_input"] = ""
    st.session_state["resume_input"] += 1

st.title("📄 Resume Roaster 3000")
st.markdown("### The AI-Powered Applicant Tracking System (ATS)")
st.markdown("This tool ranks your entire candidate pool against the job description to identify the top matches.")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Job Description")
    jd = st.text_area(
        "Paste the Job Description here:", 
        height=300, 
        key="jd_input",
        placeholder="Copy/Paste the role requirements..."
    )

with col2:
    st.subheader("2. Upload Resumes")
    resumes = st.file_uploader(
        "Upload candidate PDFs:", 
        type=['pdf'], 
        accept_multiple_files=True, 
        key=f"resume_{st.session_state['resume_input']}"
    )

st.markdown("---")

act_col1, act_col2, act_col3 = st.columns([2, 4, 1])

with act_col1:
    analyze_clicked = st.button("🚀 Analyze Candidates", type="primary")

with act_col3:
    st.button("🔄 Clear", on_click=clear_form)

if analyze_clicked:
    if not jd or not jd.strip():
        st.error("⚠️ Please paste a Job Description first.")
    elif not resumes:
        st.error("⚠️ Please upload at least one Resume PDF.")
    else:
        with st.spinner("Reading resumes and crunching numbers..."):
            
            resumes_text = []
            file_names = []
            
            progress_bar = st.progress(0)
            
            for i, file in enumerate(resumes):
                text = extract_text_from_upload(file)
                resumes_text.append(text)
                file_names.append(file.name)

                progress_bar.progress((i + 1) / len(resumes))
            

            scores = calculate_similarity(jd, resumes_text)
            
            df = pd.DataFrame({
                "Candidate": file_names,
                "Match Score": scores
            })
            
            df = df.sort_values(by="Match Score", ascending=False).reset_index(drop=True)
            df["Match Score"] = (df["Match Score"] * 100).round(2)

            st.success("Analysis Complete!")
            
            res_col1, res_col2 = st.columns([2, 2])
            
            with res_col1:
                st.subheader("🏆 Leaderboard")
                with st.container(border=True):
                    st.metric(
                        label="Top Candidate", 
                        value=df.iloc[0]['Candidate'], 
                        delta=f"{df.iloc[0]['Match Score']}% Match"
                    )
                st.dataframe(
                    df.style.background_gradient(cmap="Greens", subset=["Match Score"]), 
                    use_container_width=True
                )
                
            with res_col2:
                st.subheader("📊 Visual Comparison")
                st.bar_chart(
                    df.set_index("Candidate")["Match Score"],
                    color="#4CAF50" 
                )