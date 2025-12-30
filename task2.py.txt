salaries = list(map(int, input("Enter salaries: ").split()))

max_salary = max(salaries)
min_salary = min(salaries)

print(max_salary - min_salary)
