R = 5 
P = (2, 3)
F = (5, 5)
L = (1, 0)

points = [P, F, L]
count = 0

for x, y in points:
    if x**2 + y**2 < R**2:
        count += 1

print("Number of points inside the circle:", count)