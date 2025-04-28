# 📃 Resume Keyword Optimizer

# 🎯 Goal

Applying for jobs is already stressful - but getting past the **Applicant Tracking Systems** many companies use can be an invisible obstacle. These systems often filter out resumes that don't match enough keywords from the job description, meaning many qualified candidates with big potential are never seen and judged by a human.

**Resume Keyword Optimizer** was built to tackle this problem.
This web-based tool helps job seekers improve their chances of getting interviews by:

- Identifying **missing keywords** in their resumes based on a specific job description.
- Giving **actionable feedback** to help tailor applications for each job.
- Making **ATS optimization** more transparent, accessible, and less time-consuming.

Whether you're applying for your first internship or switching careers, this tool is designed to be simple, fast, and genuinely useful.

---

## ⚙ Features
- 📃 **Paste or Upload** your resume and a job description (`.txt`, `.docx`, `.pdf`)
- 🕵️‍♂️ **Smart Keyword Analysis**: Extracts and compares key terms automatically.
- 🔎 **Top 10 Missing Keywords** are displayed based on frequency.
- ⚠ **Critical Keywords Highlighted** if a term appears more than 5 times in the job description.
- 🌟 **Clean, professional front-end** for easy interaction.

---

## 🔧 How To use

Using **Resume Keyword Optimizer** is quick and easy - no installation required.

### Step-by-Step:
1. **Launch the Flask app locally** by running `python app.py`
2. Open your browser and go to http://127.0.0.1:5000/
2. **Paste your job description** 
3. **Paste** your job description and resume into the text boxes **or upload** .txt, .docx, or .pdf files.
4. Click **"Analyze"**.
5. Instantly view:
 - A list of **missing important keywords**
 - **Critical keywords** labeled clearly to prioritize them.
6. Go through the list and edit your resume accordingly.

---

## 💻 Technologies Used
- Python 3
- Flask
- Natural Language Toolkit (NLTK)
- python-docx (for reading Word files)
- PyMuPDF (for reading PDF files)
- HTML/CSS for front-end

--- 

## 👭 Team Members
Paulina Vasconez & Carolina Martinez

## 🖱 Requirements (for Developers)
If you want to run this project locally:

```bash
pip install flask nltk python-docx PyMuPDF


