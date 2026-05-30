# Input list to be sorted
numbers = [5, 1, 2, 4, 8]
n = len(numbers)

# Outer loop to access each list element
for i in range(n):
    # Inner loop to compare adjacent elements
    for j in range(0, n - i - 1):
        # Swap if the element is greater than the next element
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# Print the final sorted list
print("Sorted list:", numbers)
