# 📋 Resume ATS Score Checker

**An AI-powered tool to optimize resumes for Applicant Tracking Systems (ATS) and help recruiters screen candidates efficiently.**

## 🚀 Live Demo
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://resume-ats-score-checker.streamlit.app/)

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
|<img width="1406" height="817" alt="Screenshot 2026-02-04 at 6 46 30 PM" src="https://github.com/user-attachments/assets/38094075-c8b9-4a06-8991-ec5919a51f9f" /> | <img width="1421" height="864" alt="Screenshot 2026-02-04 at 6 51 00 PM" src="https://github.com/user-attachments/assets/c83ffd0e-efd5-43e3-8686-fd0b65d24197" /> |
 | <img width="813" height="385" alt="Screenshot 2026-02-04 at 6 46 53 PM" src="https://github.com/user-attachments/assets/2ea14caf-081e-4f58-b8df-5704cdb92e8c" /> | <img width="795" height="565" alt="Screenshot 2026-02-04 at 6 51 11 PM" src="https://github.com/user-attachments/assets/e606dde8-5564-420e-b249-ea40460e5ba4" /> |

---

## 🤝 Contributing

Feel free to open issues or submit pull requests if you have ideas for better visualization or new NLP features!

