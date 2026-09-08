def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index  # Return the index where the target is found
    return -1  # Return -1 if the target is not found

# Example usage:
numbers = [10, 23, 45, 70, 11, 15]
result = linear_search(numbers, 70)

if result != -1:
    print(f"Target found at index {result}")
else:
    print("Target not found")