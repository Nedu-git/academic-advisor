"""Academic Advisor System - FastAPI backend that serves the trained .pkl model."""
import pickle
from pathlib import Path

import pandas as pd
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

from advisor import GRADE_BANDS, build_advice

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "advisor_model.pkl"

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

FEATURES = ["current_cgpa", "study_hours", "attendance", "assignment_completion",
            "course_units", "sleep_hours", "extracurricular_hours"]

app = FastAPI(title="Academic Advisor System", version="1.0")


class StudentInput(BaseModel):
    current_cgpa: float = Field(..., ge=0, le=5)
    study_hours: int = Field(..., ge=0, le=80)
    attendance: int = Field(..., ge=0, le=100)
    assignment_completion: int = Field(..., ge=0, le=100)
    course_units: int = Field(..., ge=1, le=40)
    sleep_hours: float = Field(..., ge=0, le=14)
    extracurricular_hours: int = Field(..., ge=0, le=60)


@app.get("/")
def home():
    return FileResponse(BASE_DIR / "templates" / "index.html")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(student: StudentInput):
    data = student.model_dump()
    row = pd.DataFrame([data])[FEATURES]
    standing = model.predict(row)[0]
    confidence = float(model.predict_proba(row).max())
    return {
        "standing": standing,
        "gpa_band": GRADE_BANDS[standing],
        "confidence": round(confidence * 100, 1),
        "advice": build_advice(data, standing),
    }
