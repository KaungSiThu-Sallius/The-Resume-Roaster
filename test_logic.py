from src.utils import calculate_similarity

jd = "Senior Data Scientist with Python and Machine Learning"
resumes = [
    "I am a Senior Data Scientist expert in Python and ML.",
    "I am a Chef who cooks with Python snakes."
]

scores = calculate_similarity(jd, resumes)
print(f"Scores: {scores}")