n = int(input("num: "))

for num in range(1, n + 1):
    ok = True
    for d in str(num):
        if d == '0' or num % int(d) != 0:
            ok = False
            break
    if ok:
        print(num, end=' ')
