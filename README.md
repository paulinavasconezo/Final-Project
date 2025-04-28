# 📃 Resume Keyword Optimizer

# 🎯 Big Idea: Why This Project?
*Getting rejected and getting no answers before a human ever sees your resume is a frustrating experience for job seekers nowadays. As our college graduation gets closer, we, and our friends, have been on the job-hunt for a couple of months. We have experienced and seen first-hand that no amount of job applications will guarantee a job if your resume is not well formatted and worded to pass automatic filters.*

We wanted to build a tool that **makes the hidden rules of Applicant Tracking Systems (ATS) more visible and accessible.**

Applying for jobs is already stressful - but getting past the **Applicant Tracking Systems** many companies use can be an invisible obstacle. These systems often filter out resumes that don't match enough keywords from the job description, meaning many qualified candidates with big potential are never seen and judged by a human.

**Resume Keyword Optimizer** was built to tackle this problem. This web-based tool helps job seekers improve their chances of getting interviews by:

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

## 🖼 Results
**Homepage**
*Insert screenshot here*
**Results Page**
*Insert screenshot here*

## 📈 Project Evolution
Throughout the development process, we improved and expanded the project to meet real-world user needs:
- Added **file upload support** for `.txt`, `.docx`, and `.pdf`
- Introduced **critical keyword highlighting** to prioritize essential words.
- Refined **front-end styling** for a clean and user-friendly interface
- Improved **NLP Processing** with a custom stopword list to focus on important terms.

We learned the importance of iteration, user perspective, and making technical tools accessible through a simple user interface.

---
## 📶 Live Demo
*If Render website works we will replace this line with:*
Access the Live Demo here! 🚀

## 💻 Technologies Used
- Python 3
- Flask
- Natural Language Toolkit (NLTK)
- python-docx (for reading Word files)
- PyMuPDF (for reading PDF files)
- HTML/CSS for front-end

--- 
## 🤖 Use of AI
Throughout the development of this project, we used OpenAI's ChatGPT as a resource to enhance and guide our work. 

Specifically, ChatGPT helped with:
- Debugging Flask application issues, such as handling file uploads and routing between pages.
- Expanding functionality beyond the original plan including support for how to download the requirements to allow users to upload `.txt` `.docx` and `.pdf` files.
- Improving NLP steps, like cleaning and tokenizing text and coming up with a fuller list of custom stopwords that are commonly repeated in job descriptions.
- Suggesting changes and edits in our html pages, such as addding `div` and using  `class` attributes to be able to easily style our pages.
- Troubleshooting deployment issues on Render, including resolving problems with port binding and configuring the app to run successfully on a live server.

Overall, ChatGPT was useful as a development tutor in helping troubleshoot problems, explore different technical solutions, brainstorm improvements, and enhance the overall quality of the final deliverable.

## 👭 Team Members
Paulina Vasconez & Carolina Martinez

## 🖱 Requirements (for Developers)
If you want to run this project locally:

```bash
pip install flask nltk python-docx PyMuPDF


