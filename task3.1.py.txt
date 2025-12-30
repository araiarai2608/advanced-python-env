import math
a1, b1 = 3, 4
a2, b2 = 5, 12
hyp1 = math.sqrt(a1**2 + b1**2)
hyp2 = math.sqrt(a2**2 + b2**2)

print("Hypotenuse of triangle 1:", hyp1)
print("Hypotenuse of triangle 2:", hyp2)

if hyp1 > hyp2:
    print("Trian1 has greater hypotenuse")
elif hyp1 < hyp2:
    print("Trian2 has greater hypotenuse")
else:
    print("Both hypotenuses are equal")
