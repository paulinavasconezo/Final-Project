from flask import Flask, render_template, request
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
from collections import Counter

from docx import Document
import fitz

nltk.download('punkt_tab')
nltk.download('stopwords')

app = Flask(__name__)

custom_stopwords = set([
    'organization', 'strong', 'including', 'status', 'channels', 'campaigns', 'campaign',
    'first', 'skills', 'team', 'role', 'position', 'responsibilities', 'requirements',
    'required', 'preferred', 'experience', 'ability', 'must', 'work', 'job', 'opportunity',
    'management', 'communication', 'professional', 'business', 'strategic', 'planning',
    'implement', 'support', 'develop', 'various', 'process', 'services', 'operations',
    'related', 'field', 'understanding', 'knowledge', 'ensure', 'assist', 'employer', 'build', 'recruitment', 'key', 'execution', 'workforce', 'client', 'office', 'impact', 'clients','help','join', 'bonus'
])

def extract_text_from_docx(file):
    doc = Document(file)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

def extract_text_from_pdf(file):
    text = ""
    pdf_document = fitz.open(stream=file.read(), filetype="pdf")
    for page in pdf_document:
        text += page.get_text()
    return text

def clean_and_tokenize(text):
    """This function turns words into tokens and gets rid of stopwords"""
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    cleaned_tokens= [
        word for word in tokens
        if word.isalpha() and word not in stop_words
    ]
    return set(cleaned_tokens)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():

    job_text = request.form['job']
    job_file = request.files.get('job_file')
    if job_file:
        filename = job_file.filename.lower()
        if filename.endswith('.txt'):
            job_text = job_file.read().decode('utf-8')
        elif filename.endswith('.docx'):
            job_text = extract_text_from_docx(job_file)
        elif filename.endswith('.pdf'):
            job_text = extract_text_from_pdf(job_file)

    resume_text = request.form['resume']
    resume_file = request.files.get('resume_file')
    if resume_file:
        filename = resume_file.filename.lower()
        if filename.endswith('.txt'):
            resume_text = resume_file.read().decode('utf-8')
        elif filename.endswith('.docx'):
            resume_text = extract_text_from_docx(resume_file)
        elif filename.endswith('.pdf'):
            resume_text = extract_text_from_pdf(resume_file)

    resume_words = clean_and_tokenize(resume_text)
    job_words = clean_and_tokenize(job_text)

    missing_keywords = list(job_words - resume_words) 

    job_tokens = word_tokenize(job_text.lower())
    stop_words = set(stopwords.words('english')).union(custom_stopwords)
    job_tokens_clean = [
        word for word in job_tokens
        if word.isalpha() and word not in stop_words
    ]

    word_freq = Counter(job_tokens_clean)

    sorted_missing = sorted(
        missing_keywords,
        key=lambda word: word_freq[word],
        reverse=True
    )

    top_missing_keywords = [(word, word_freq[word]) for word in sorted_missing[:10]]

    print("Top missing keywords:", top_missing_keywords)

    return render_template('result.html', missing_keywords=top_missing_keywords)

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
