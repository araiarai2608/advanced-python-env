import numpy as np

numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Array:", numbers)

total_sum = numbers.sum()
print("Sum of elements:", total_sum)

average_value = numbers.mean()
print("Mean value:", average_value)

max_value = numbers.max()
print("Maximum element:", max_value)

multiplied_by_two = numbers * 2
print("Array multiplied by 2:", multiplied_by_two)

modified_array = numbers.copy()
for i in range(len(modified_array)):
    if modified_array[i] > 5:
        modified_array[i] = -1

print("Array after replacing values greater than 5:", modified_array)