items = input().split()

counts = {}
for i in items:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1

print("Purchase num:")
for i, c in counts.items():
    print(f"{i}: {c}")

most = max(counts, key=counts.get)
print(f"Most putchaced item: {most}")

once = []
for i, c in counts.items():
    if c == 1:
        once.append(i)
print("Purchased once:", " ".join(once))

sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
print("Sorted by count:")
for i, c in sorted_counts:
    print(i, c)
