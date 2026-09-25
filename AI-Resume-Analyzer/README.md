# AI Resume Analyzer

AI-powered resume analyzer and job matcher built with React, FastAPI, Python, NLP, and scikit-learn.

## Features

- Upload a resume PDF
- Extract resume text
- Detect common technical skills
- Parse job descriptions
- Separate required and preferred skills
- Calculate skill-match score
- Calculate TF-IDF text similarity
- Generate skill-gap recommendations
- React dashboard for analysis results

## Project Structure

```text
AI-Resume-Analyzer/
├── backend/
│   ├── main.py
│   ├── matcher.py
│   ├── matching_engine.py
│   ├── pdf_reader.py
│   ├── resume_parser.py
│   ├── job_parser.py
│   ├── recommendation_engine.py
│   └── requirements.txt
└── frontend/
    ├── src/
    ├── index.html
    ├── package.json
    └── vite.config.js
```

## Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend runs at `http://127.0.0.1:8000`.

## Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at `http://localhost:5173`.

## Matching Method

Version 1 uses a transparent hybrid approach:

- Rule-based skill extraction
- Required/preferred skill matching
- TF-IDF vectorization
- Cosine similarity
- Weighted scoring

The current overall score uses 60% skill matching and 40% text similarity.

## Future Improvements

- Better NLP-based requirement extraction
- Semantic embeddings
- Experience matching
- Education matching
- Dynamic score visualization
- Resume improvement suggestions
- Deployment
