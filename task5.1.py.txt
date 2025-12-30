A, B = 3, 4
C, D = 1, 6

num = A * D - B * C
den = B * D

a, b = abs(num), den
while b != 0:
    a, b = b, a % b
g = a

num = num // g
den = den // g

print(f"{A}/{B} - {C}/{D} = {num}/{den}")

