s = input()
t = 0

for i in range(len(s)):
    if s[i:i+5] == ">>-->":
        t += 1
    if s[i:i+5] == "<--<<":
        t += 1

print(t)
