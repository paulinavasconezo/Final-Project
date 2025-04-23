from flask import Flask, render_template, request
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt_tab')
nltk.download('stopwords')


app = Flask(__name__)

def clean_and_tokenize(text):
    """This function turns words into tokens and get rid of stopwords"""
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
    resume_text = request.form['resume']
    job_text = request.form['job']

    resume_words = clean_and_tokenize(resume_text)
    job_words = clean_and_tokenize(job_text)
    
    print("Resume words:", resume_words)
    print("Job words:", job_words)

    missing_keywords = sorted(list(job_words - resume_words))
    print("Missing keywords:", missing_keywords)

    return render_template('result.html', missing_keywords=missing_keywords)


if __name__ == '__main__':
    app.run(debug=True)
