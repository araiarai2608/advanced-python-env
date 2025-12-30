A, B = 2, 3
C, D = 4, 5

num = A * D
den = B * C

a, b = num, den
while b != 0:
    a, b = b, a % b
g = a

num = num // g
den = den // g

print(f"{A}/{B} ÷ {C}/{D} = {num}/{den}")