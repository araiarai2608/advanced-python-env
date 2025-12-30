import math

r = float(input())
a = float(input())
b = float(input())
h = float(input())

print(math.pi*r*r)
print(a*b)
print(a*h/2)

for i in range(3):
    arr = list(map(int, input().split()))
    print(sum(arr), sum(arr)/len(arr))
