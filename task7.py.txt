a = float(input("First number: "))
op = input("Operation (+, -, *, /): ")
b = float(input("Second number: "))

if op == "/" and b == 0:
    print("Error: division by zero")
elif op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("Unknown operation")
