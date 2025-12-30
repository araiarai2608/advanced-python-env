n = int(input())
letters = "ABCEHKMOPTXY"
nums = "0123456789"

for _ in range(n):
    s = input()
    if len(s) != 6:
        print("No")
        continue
    if s[0] not in letters:
        print("No")
        continue
    if s[1] not in nums or s[2] not in nums or s[3] not in nums:
        print("No")
        continue
    if s[4] not in letters or s[5] not in letters:
        print("No")
        continue
    print("Yes")
