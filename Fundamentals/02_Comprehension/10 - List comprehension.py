# List comprehension with conditional logic
''' This code demonstrates how to use list comprehension in Python, which provides a concise way to create or modify lists.
    In this case, it modifies the elements of 'list1' based on whether they are even or odd. '''

# Initial list with integers
list1 = [1, 3, 4, 5, 6, 7, 8]

# Empty list to store the transformed values
list2 = []

# Original loop approach (commented out)
# The loop iterates through each element in 'list1', checks if it's even or odd, and modifies it accordingly.
# for i in list1:
#     if i % 2 == 0:
#         list2.append(i)  # If the number is even, append it unchanged
#     else:
#         list2.append(i + 1)  # If the number is odd, add 1 to make it even

# Using list comprehension to achieve the same result in a more concise manner
list2 = [i if i % 2 == 0 else i + 1 for i in list1]
# Explanation: For each element 'i' in 'list1', if 'i' is even (i.e., i % 2 == 0), it remains unchanged.
# If 'i' is odd, we add 1 to it to make it even.

# Print the resulting list using unpacking
# The '*' operator is used to unpack the list so that its elements are printed separately.
print(*list2)
# Expected Output: 2 4 4 6 6 8 8
