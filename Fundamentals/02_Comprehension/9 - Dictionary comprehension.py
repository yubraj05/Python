# This script demonstrates various ways to create and manipulate dictionaries in Python, 
# including basic assignments, dictionary comprehensions, conditional logic within comprehensions, 
# and nested dictionary comprehensions.

# Simple dictionary creation using a for loop
dict1 = {}
for i in range(1, 11):  # Iterate over numbers from 1 to 10
    dict1[i] = i * 2  # Assign each number's double as the value for the corresponding key
print(dict1)  # Output the dictionary

# Dictionary comprehension to achieve the same result in a more compact form
dict1 = {i: i * 2 for i in range(1, 11)}  # Create a dictionary with keys 1 to 10, values as the double of the key
print(dict1)  # Output the dictionary

# Dictionary comprehension with a condition to include only even numbers
dict1 = {i: i * 2 for i in range(1, 11) if i % 2 == 0}  
# Includes only even numbers from 1 to 10, with values as their double
print(dict1)  # Output the dictionary

# Using an if-else expression inside a dictionary comprehension to modify values based on a condition
dict1 = {i: i * 2 if i % 2 == 0 else i + 1 for i in range(1, 11)}  
# If the number is even, its value is the double; if it's odd, the value is the number + 1
print(dict1)  # Output the dictionary

# Nested dictionary comprehension: creating a dictiona
