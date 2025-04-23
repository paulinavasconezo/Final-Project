# Resume Keyword Optimizer

## Big Idea
This project is a Python-based web application that helps people looking for jobs optimize their resumes for specific job descriptions. By analyzing the overlap between the resume and the job posting, the app identifies missing keywords to improve the user's chances of passing Applicant Tracking Systems screenings.

Topics to explore:
- Natural Language Processing techniques
- Flask web application development
- Basic front-end development with HTML/CSS

Minimum Viable Product:
- A working web application with two input fields (job description and resume)
- Backend text processing
- Display a list of missing important keywords in the resume

Stretch Goals:
- Offer synonym suggestions for missing keywords
- Allow users to upload .txt or .pdf files instead of pasting text manually

---

## Learning Objectives

### Shared Goals
- Apply the principles of software design to a real-world problem that many students face as applying to jobs becomes more competitive and oversaturated.

### Individual Goals
- Be able to use this application in my personal job search and hope that it does provide useful help in tailoring my resume for every specific job. (Carolina)
- I want to help my friends increase their possibilities to get a job and land an interviews since computerized job application processes have hurt this opportunity for many people.

## Implementation Plan

### Technologies Planned:
- Python 3 for backend development
- Flask to build the web app
- HTML and CSS for the front-end
- NLTK

### Execution Plan
- Start with a tokenizer to split words and remove stopwords
- Build Flask program to accept form inputs and return analysis results
- Investigate using NLTK's existing stopword lists and tokenization methods

## Project Schedule

- April 12 - 14: Finalize project idea, set up GitHub repository, basic Flask app
- April 15 - 19: Implement minimum viable product: input forms, text processing, keyword comparison
- April 20 - 24: Create front-end result display, clean interface improvements, test MVP functionality
- April 25 - 30: Add optional stretch goals
- May 1 - 3: Final bug fixes, polishing, and submission

## Collaboration Plan
This project will be completed by Paulina and Carolina as a group. To stay on track we will follow our execution plan and project schedule. We will meet every week in-person to work on it together and collaborate in a faster way. We won't divide the work because we want to ensure that everything works together seamlessly, so we prefer combining both of our knowledge to get the best product.

## Risks and Limitations
- Natural Language Processing: Accurately identifying the meaninful keywords while filtering out irrelevant words can get tricky.
- Front-end: Making the output intuitive and clean, finding the balance between the back-end and functionality and the front-end and user experience.

To address these challenges we will prioritiz building a very simple, but finctional MVP before adding any stretch features. We will also try to keep the front-end simple and focus on clear information display instead of design-heavy features. We will try to implement any new knowledge we gained after doing Assignment 3 to help us in this process.