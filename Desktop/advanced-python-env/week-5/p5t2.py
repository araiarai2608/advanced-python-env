import json

with open("students.json", "r") as f:
    students = json.load(f)

for student in students:
    grades = student["grades"]
    average = sum(grades) / len(grades)
    student["average"] = average

with open("students_average.json", "w") as f:
    json.dump(students, f, indent=4)
