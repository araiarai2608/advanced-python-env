A = 12
B = 18

a, b = A, B
while b != 0:
    a, b = b, a % b
gcd = a

lcm = (A * B) // gcd

print(f"gcd of {A} and {B} is {gcd}")
print(f"lcm of {A} and {B} is {lcm}")
