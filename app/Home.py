import streamlit as st

st.set_page_config(page_title="Resume Roaster Hub", page_icon="🤖")

st.title("🤖 Resume Roaster AI")
st.markdown("### Choose your mode from the sidebar")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 🚀 For Job Seekers")
    st.info("Select **'Job Seeker'** to optimize your own resume against a job description.")

with col2:
    st.markdown("#### 👔 For Recruiters")
    st.success("Select **'Recruiter'** to upload a stack of resumes and rank the best candidates.")