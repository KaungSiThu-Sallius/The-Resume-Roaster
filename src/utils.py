import re
import nltk
from PyPDF2 import PdfReader
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

try: 
    nltk.data.find('corpora/stopwords')
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('punkt_tab')

def extract_text_from_upload(uploaded_file):
    """
    Input: 
        - uploaded_file: StreamlitUploadedFile object 
    Output: 
        - full_text: String 
    """
    try:
        reader = PdfReader(uploaded_file)
        full_text = ""
        for page in reader.pages:
            text = page.extract_text()
            full_text += text
        return full_text

    except Exception as e:
        print("Failed to read one or more pdf files.", e)



def clean_text(data):
    """
    Input: 
        - data: String 
    Output: 
        - final_cleaned_data: String 
    """
    cleaning_txt01 = data.replace('\n', '').lower()
    cleaning_txt02 = re.sub(r'[^a-z0-9 ]', '', cleaning_txt01)
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(cleaning_txt02)
    filtered_tokens = [word for word in tokens if word not in stop_words]
    final_cleaned_data = " ".join(filtered_tokens)
    return final_cleaned_data

def calculate_similarity(job_description, resumes):
    """
    Input: 
        - job_description: String 
        - resumes_list: List of Strings 
    Output: 
        - scores: List of floats 
    """
    jd_cleaned = clean_text(job_description)
    resumes_cleaned = [clean_text(text) for text in resumes]
    corpus = [jd_cleaned] + resumes_cleaned
    vectorizer = TfidfVectorizer()
    doc_matrix = vectorizer.fit_transform(corpus)
    similarity_scores = cosine_similarity(doc_matrix[0:1], doc_matrix)
    return similarity_scores[0][1:]
    