m = int(input("array length: "))

A = []
for i in range(m):
    A.append(int(input()))

print("original array:", A)

A[0], A[-1] = A[-1], A[0]

print("final array:", A)
