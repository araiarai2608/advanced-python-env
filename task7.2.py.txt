n = int(input("num int "))

octal_code = ""
temp = n
for _ in range(10): 
    octal_code = str(temp % 8) + octal_code
    temp = temp // 8

print("10-digit octal code:", octal_code)
