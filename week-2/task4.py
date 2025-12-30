a, b = map(int, input().split())
text = input()

words = set()
for i in range(a - b + 1):
    words.add(text[i:i+b])

print(len(words))