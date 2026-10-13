"""Rule-based advice engine. Combines the ML prediction with simple, explainable rules."""

GRADE_BANDS = {
    "First Class": "4.50 - 5.00",
    "Second Class Upper": "3.50 - 4.49",
    "Second Class Lower": "2.40 - 3.49",
    "Third Class / At Risk": "below 2.40",
}


def build_advice(student: dict, standing: str) -> list[str]:
    tips = []

    if standing == "Third Class / At Risk":
        tips.append("You are at risk. Book a meeting with your course adviser this week and agree on a recovery plan.")
    elif standing == "Second Class Lower":
        tips.append("You are close to Second Class Upper. Small, steady improvements in your habits will move you up.")
    elif standing == "Second Class Upper":
        tips.append("Good work. Stay consistent and target your weakest courses to push towards First Class.")
    else:
        tips.append("Excellent. Protect this standing by keeping your current routine and helping others (teaching reinforces learning).")

    if student["study_hours"] < 10:
        tips.append(f"You study {student['study_hours']} hrs/week. Aim for at least 15: about 2 hours a day, split into focused 45-minute blocks.")
    if student["attendance"] < 75:
        tips.append(f"Attendance is {student['attendance']}%. Many courses require 75% to sit exams - prioritise lectures.")
    if student["assignment_completion"] < 80:
        tips.append(f"You complete {student['assignment_completion']}% of assignments. Continuous assessment is free marks - use a planner for deadlines.")
    if student["course_units"] > 24:
        tips.append(f"{student['course_units']} units is a heavy load. Plan your timetable early and start revising difficult courses first.")
    if student["sleep_hours"] < 6:
        tips.append(f"{student['sleep_hours']} hrs of sleep is too little. 7-8 hours improves memory and exam performance.")
    elif student["sleep_hours"] > 9.5:
        tips.append("You may be oversleeping. Move some of that time into a fixed study slot.")
    if student["extracurricular_hours"] > 12:
        tips.append(f"{student['extracurricular_hours']} hrs/week on extracurriculars is high. Cut back during exam periods.")

    if len(tips) == 1:
        tips.append("Your habits look balanced. Keep tracking them every semester.")
    return tips
