import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

GOOD_STUDENT = {"current_cgpa": 4.7, "study_hours": 25, "attendance": 95, "assignment_completion": 100,
                "course_units": 20, "sleep_hours": 7.5, "extracurricular_hours": 4}
WEAK_STUDENT = {"current_cgpa": 1.6, "study_hours": 3, "attendance": 50, "assignment_completion": 40,
                "course_units": 28, "sleep_hours": 4.5, "extracurricular_hours": 18}


def test_health():
    assert client.get("/health").json() == {"status": "ok"}


def test_home_page_loads():
    r = client.get("/")
    assert r.status_code == 200
    assert "Academic Advisor System" in r.text


def test_strong_student_predicted_high():
    r = client.post("/predict", json=GOOD_STUDENT).json()
    assert r["standing"] in ("First Class", "Second Class Upper")
    assert len(r["advice"]) >= 1


def test_weak_student_gets_warnings():
    r = client.post("/predict", json=WEAK_STUDENT).json()
    assert r["standing"] in ("Third Class / At Risk", "Second Class Lower")
    assert len(r["advice"]) >= 4


def test_invalid_input_rejected():
    bad = dict(GOOD_STUDENT, current_cgpa=7.0)
    assert client.post("/predict", json=bad).status_code == 422
