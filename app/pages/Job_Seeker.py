import sys
import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Add the project root to the python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.utils import extract_text_from_upload, calculate_similarity

st.set_page_config(page_title="Resume Optimizer", page_icon="🚀")

if "resume_input" not in st.session_state:
    st.session_state['resume_input'] = 0

def clear_form():
    st.session_state["jd_input"] = ""
    st.session_state["resume_input"] += 1

st.title("🚀 Resume Optimizer")
st.markdown("### Don't apply blindly. Check your fit score first.")
st.markdown("This tool compares your resume against the job description to estimate your ATS match rate.")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Your Resume")
    uploaded_file = st.file_uploader(
        "Upload your PDF:", 
        type=['pdf'], 
        key=f"resume_{st.session_state['resume_input']}",
        accept_multiple_files=False 
    )

with col2:
    st.subheader("2. The Job")
    jd = st.text_area(
        "Paste Job Description:", 
        height=300, 
        key="jd_input",
        placeholder="Paste the job description here..."
    )

st.markdown("---")

act_col1, act_col2, act_col3 = st.columns([2, 4, 1])

with act_col1:
    analyze_clicked = st.button("✔️ Check My Score", type="primary")

with act_col3:
    st.button("🔄 Clear", on_click=clear_form)

if analyze_clicked:
    if not jd or not jd.strip():
        st.error("⚠️ Please paste the Job Description.")
    elif not uploaded_file:
        st.error("⚠️ Please upload your Resume.")
    else:
        with st.spinner("Analyzing your profile..."):
            
            resume_text = extract_text_from_upload(uploaded_file)

            scores = calculate_similarity(jd, [resume_text])
            match_score = round(scores[0] * 100, 2)
            
            st.markdown("### 📊 Your Results")
            
            if match_score >= 50:
                st.success(f"🔥 Excellent Match! Your Score: {match_score}%")
                st.balloons()
            elif match_score >= 20:
                st.info(f"✅ Good Start. Your Score: {match_score}%")
            else:
                st.warning(f"⚠️ Low Match. Your Score: {match_score}%")

            with st.container(border=True):
                col_res1, col_res2 = st.columns(2)
                with col_res1:
                    st.metric(label="Match Score", value=f"{match_score}%")
                with col_res2:
                    st.metric(label="File Analyzed", value=uploaded_file.name)

            st.subheader("💡 Analysis")
            if match_score < 20:
                st.write("Your resume is missing key terms found in the job description. Consider tailoring your 'Skills' section.")
            else:
                st.write("Your resume aligns well with this role. Good luck!")