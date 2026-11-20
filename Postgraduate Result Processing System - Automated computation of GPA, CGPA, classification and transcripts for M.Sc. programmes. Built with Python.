import pandas as pd

def grade_point(score):
    if score >= 70:
        return 5.0, "A"
    elif score >= 60:
        return 4.0, "B"
    elif score >= 50:
        return 3.0, "C"
    elif score >= 45:
        return 2.0, "D"
    elif score >= 40:
        return 1.0, "E"
    else:
        return 0.0, "F"

def classify(cgpa):
    if cgpa >= 4.5:
        return "Distinction"
    elif cgpa >= 3.5:
        return "Merit / Upper Credit"
    elif cgpa >= 2.5:
        return "Lower Credit"
    elif cgpa >= 1.0:
        return "Pass"
    else:
        return "Fail"

def calculate_gpa(courses):
    total_points = 0
    total_units = 0
    results = []
    for code, unit, score in courses:
        gp, grade = grade_point(score)
        total_points += gp * unit
        total_units += unit
        results.append({"Course": code, "Unit": unit, "Score": score, "Grade": grade, "Point": gp})
    gpa = total_points / total_units if total_units else 0
    return round(gpa, 2), pd.DataFrame(results)

student = {
    "Name": "John Doe",
    "Reg No": "PG/MSc/CS/001",
    "Programme": "M.Sc. Computer Science",
    "Session": "2024/2025"
}

courses_sem1 = [
    ("CSC 801", 3, 72),
    ("CSC 802", 3, 65),
    ("CSC 803", 2, 58),
    ("CSC 804", 3, 80),
]

gpa, df = calculate_gpa(courses_sem1)
print(f"Student: {student['Name']} ({student['Reg No']})")
print(df.to_string(index=False))
print(f"\nGPA: {gpa}")
print(f"Classification: {classify(gpa)}")
df.to_csv("transcript.csv", index=False)
print("\nTranscript saved as transcript.csv")
