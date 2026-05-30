

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


# Initialize an unsorted list
arr = [12, 11, 13, 5, 6]

# Outer loop: Start from the second element (index 1) to the end
for i in range(1, len(arr)):
    key = arr[i]  # The element to be positioned
    j = i - 1     # Index of the element to the left
    
    # Inner loop: Move elements that are greater than key to one position ahead
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
        
    # Place the key in its correct sorted position
    arr[j + 1] = key

# Print the final sorted list
print("Sorted list:", arr)
