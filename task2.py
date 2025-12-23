a = input()
b = input()
n = len(b)
bb = b + b
c = 0

for i in range(len(a) - n + 1):
    if a[i:i+n] in bb:
        c += 1

print(c)
