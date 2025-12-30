import math

a = int(input())
b = int(input())
c = int(input())
d = int(input())
p = int(input())

s1 = (a + b + p) / 2
val1 = s1 * (s1 - a) * (s1 - b) * (s1 - p)
area1 = math.sqrt(val1) if val1 > 0 else 0

s2 = (c + d + p) / 2
val2 = s2 * (s2 - c) * (s2 - d) * (s2 - p)
area2 = math.sqrt(val2) if val2 > 0 else 0

print("area of quadrilateral:", area1 + area2)