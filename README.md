# Monthly Project Charter: January

**Project Name:** The Resume Roaster  
**Goal:** An automated keyword analysis tool for job seekers.

---

## 1. The Problem

* **What specific problem are we solving?** Job seekers apply into the "void" of Applicant Tracking Systems (ATS) and get rejected because they lack specific keywords, even if they are qualified.
* **Who is the user?** Job Seekers and Junior Recruiters.
* **Why does this need Data Science?** Simple string matching fails on synonyms or frequency. We need vectorization (converting text to numbers) to measure "similarity" mathematically.

## 2. The Solution (MVP)

**Input:**
* Text area for the Job Description.
* File Uploader for the Resume (PDF).

**Model Approach:**
* Text Extraction (PyPDF2).
* Cleaning (Stopword removal, Lemmatization via Spacy/NLTK).
* Vectorization (TF-IDF).
* Similarity Scoring (Cosine Similarity).

**Output:** A percentage match score (0-100%) and a list of "Missing Key Terms."

## 3. Success Metrics

* **Deployment:** App is live on Streamlit Cloud.
* **Reliability:** The app handles weird PDF formats without crashing.
* **Performance:** Analysis completes in < 3 seconds.

## 4. Tech Stack

* **Data Source:** User uploads + Kaggle (for testing dataset).
* **Model Library:** Scikit-Learn (Feature Extraction), NLTK/Spacy.
* **Frontend:** Streamlit.
* **Deployment:** Streamlit Cloud (easiest for Month 1).