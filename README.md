# Academic Advisor System (CSC 303)

An academic advisor that combines **software engineering practices** (Git/GitHub version control,
virtual environment, requirements file, automated tests, clean project structure) with an
**AI technique** (a Random Forest classifier trained on Google Colab).

The user enters their CGPA and study habits. The model predicts their likely degree standing
(First Class, Second Class Upper, Second Class Lower, Third Class / At Risk) and a rule-based
engine gives personalised advice.

## Project structure
```
academic-advisor/
├── notebooks/advisor_model_training.ipynb  # model built on Google Colab
├── advisor_model.pkl                       # trained model (downloaded from Colab)
├── main.py                                 # FastAPI backend (serves the model)
├── advisor.py                              # rule-based advice engine
├── templates/index.html                    # web application front end
├── tests/test_api.py                       # automated tests (pytest)
├── requirements.txt
└── .gitignore
```

## Run locally
```bash
python -m venv venv
venv\Scripts\activate          # Windows  (Mac/Linux: source venv/bin/activate)
pip install -r requirements.txt
uvicorn main:app --reload
```
Open http://127.0.0.1:8000 for the web app, or http://127.0.0.1:8000/docs for the API docs.

## Run tests
```bash
pytest
```

## Tech stack
Python · scikit-learn · pandas · numpy · FastAPI · Uvicorn · Google Colab · Git & GitHub · VS Code

Author: Chinedu Emmanuel Igbosopulu
