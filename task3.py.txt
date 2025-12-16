a = float(input("Enter a number: "))

integer_part = int(a)
fractional_part = round(a - integer_part, 2)

new_number = fractional_part * 100 + integer_part / 100

print(new_number)

