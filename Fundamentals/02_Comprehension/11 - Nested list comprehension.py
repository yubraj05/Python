# List Comprehensions for Nested Lists and Flattening
''' This code demonstrates the use of nested list comprehensions to create multi-dimensional lists and flatten them. '''

# Example 1: Creating a 2D list (3 rows, 5 columns)
lst = [[i for i in range(1, 6)] for l in range(3)]
# Explanation:
# - The outer list comprehension `[... for l in range(3)]` creates 3 sublists (i.e., 3 rows).
# - The inner list comprehension `[i for i in range(1, 6)]` creates a list of integers from 1 to 5 (i.e., 5 columns).
# This results in a 3x5 2D list.

print(lst)
# Expected Output: [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]

# Example 2: Creating a 2D list with a pattern (3 rows, 3 columns)
lst1 = [[i + m for i in range(1, 4)] for m in range(3)]
# Explanation:
# - The outer list comprehension `[... for m in range(3)]` iterates over `m` for 3 times (i.e., 3 rows).
# - The inner list comprehension `[i + m for i in range(1, 4)]` creates lists where each element is `i + m` (i.e., values from 1 to 3 incremented by `m`).
# This results in a 3x3 2D list where the values are shifted by `m` for each row.

print(lst1)
# Expected Output: [[1, 2, 3], [2, 3, 4], [3, 4, 5]]

# Example 3: Flattening a 2D list (Converting it into a 1D list)
flat_list = [item for sublist in lst1 for item in sublist]
# Explanation:
# - The outer loop (`for sublist in lst1`) iterates over each sublist in `lst1`.
# - The inner loop (`for item in sublist`) iterates over each item in the current sublist.
# - This flattens the 2D list into a 1D list by extracting each item from every sublist.
# The result is a flattened version of `lst1`.

print(flat_list)
# Expected Output: [1, 2, 3, 2, 3, 4, 3, 4, 5]
