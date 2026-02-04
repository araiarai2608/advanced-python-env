import pandas as pd

student_names = ["Arailym", "Alisher", "Alikhan", "Dimash", "Ali"]
student_ages = [19, 19, 19, 19, 19]
exam_scores = [85, 90, 78, 88, 95]

students_data = {
    "Name": student_names,
    "Age": student_ages,
    "Score": exam_scores
}

students_df = pd.DataFrame(students_data)

print("Students table:")
print(students_df)

print("\nFirst three records:")
print(students_df.iloc[:3])

average_score = sum(exam_scores) / len(exam_scores)
print("\nAverage exam score:", average_score)

print("\nStudents older than 20 years:")
older_students = students_df[students_df["Age"] > 20]
print(older_students)

print("\nStudents with score above 80:")
high_score_students = students_df[students_df["Score"] > 80]
print(high_score_students)