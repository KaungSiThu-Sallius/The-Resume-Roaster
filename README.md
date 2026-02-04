# 📋 Resume ATS Score Checker

**An AI-powered tool to optimize resumes for Applicant Tracking Systems (ATS) and help recruiters screen candidates efficiently.**

## 🚀 Live Demo
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://the-resume-roaster-kaungsithu.streamlit.app/)

---

## 📖 Overview
The **Resume ATS Checker** is a full-stack data science application designed to solve the "black box" problem of hiring. It uses **Natural Language Processing (NLP)** to quantify the match between a resume and a job description.

The tool serves two personas:
1.  **Job Seekers:** Analyze your resume against a target job to get an estimated "ATS Match Score" and feedback.
2.  **Recruiters:** Upload a batch of resumes to instantly rank candidates and identify the top matches.

---

## ✨ Features

### 1. For Job Seekers (ATS Score Checker)
* **Single-Resume Analysis:** Upload your PDF and paste the Job Description.
* **Match Result:** Instant percentage score based on semantic relevance.
* **Feedback System:** 
    * 🟢 **>40%:** Excellent Match (High probability of  ATS)
    * 🟡 **20-40%:** Good Start (Needs keyword optimization)
    * 🔴 **<20%:** Low Match (Missing critical skills)

### 2. For Recruiters (Candidate Ranking Tool)
* **Bulk Upload:** Process multiple PDF resumes simultaneously.
* **Leaderboard:** Automatically ranks candidates from highest to lowest fit.
* **Visual Data:** Interactive bar charts to compare candidate scores at a glance.

---

## 🧠 How It Works
Unlike simple keyword counters, this project uses **Cosine Similarity** on **TF-IDF Vectors**.

1.  **Text Extraction:** Uses `PyPDF2` to scrape raw text from PDF files.
2.  **Cleaning:** Removes stopwords (common words like "and", "the") using `NLTK`.
3.  **Vectorization:** Converts the Job Description and Resumes into mathematical vectors using `TfidfVectorizer` (Term Frequency-Inverse Document Frequency).
4.  **Similarity Calculation:** Calculates the cosine of the angle between the vectors. 
    * Closer to 1 (0°) = High Similarity (Perfect Match).
    * Closer to 0 (90°) = No Similarity.

---

## 🛠️ Tech Stack
* **Frontend:** [Streamlit](https://streamlit.io/) 
* **Language:** Python
* **NLP & ML:** Scikit-Learn, NLTK
* **Data Manipulation:** Pandas
* **PDF Parsing:** PyPDF2

---

## 💻 Local Installation

If you want to run this app on your own machine:

**1. Clone the repository**
```bash
git clone https://github.com/KaungSiThu-Sallius/The-Resume-Roaster.git
cd The-Resume-Roaster
```

**2. Install Dependencies**
This project uses `pipenv` for dependency management.

```bash
pipenv install
pipenv shell
```

**3. Run the App**

```bash
streamlit run app/main.py
```

---

## 📂 Project Structure

```text
The-Resume-Roaster/
├── app/
|   ├── Home.py 
│   └── pages/
│       ├── Job_Seeker.py       
│       └── Recruiter.py                    
├── data/
│   ├── cleaned/                
│   └── raw/                   
├── notebooks/
│   ├── 01_data_preparation.ipynb
│   └── 02_modelling.ipynb
├── src/
│   ├── __init__.py
│   └── utils.py              
├── .gitignore
├── Pipfile                 
├── Pipfile.lock              
├── README.md                 
└── test_logic.py              
```

---

## 📸 Screenshots

| Job Seeker Dashboard | Recruiter Leaderboard |
| --- | --- |
| *(Add screenshot here)* | *(Add screenshot here)* |

---

## 🤝 Contributing

Feel free to open issues or submit pull requests if you have ideas for better visualization or new NLP features!

