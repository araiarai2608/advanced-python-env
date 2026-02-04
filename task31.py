import matplotlib.pyplot as plt

names = ["Arailym", "Alisher", "Alikhan", "Dimash", "Ali"]
scores = [85, 90, 78, 88, 95]

plt.figure()
plt.plot(names, scores, marker='o')
plt.xlabel("Student Names")
plt.ylabel("Exam Scores")
plt.title("Line Chart of Student Scores")
plt.grid(True)
plt.show()

plt.figure()
plt.bar(names, scores)
plt.xlabel("Student Names")
plt.ylabel("Exam Scores")
plt.title("Bar Chart of Student Scores")
plt.xticks(rotation=45)
plt.show()
