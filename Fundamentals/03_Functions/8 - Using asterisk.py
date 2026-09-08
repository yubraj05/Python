# ------------------------ Unpacking in Assignments -----------------------------
''' This section demonstrates how to use the unpacking feature in Python to assign values 
    from an iterable into variables. The `*` operator allows for capturing a variable 
    number of elements from the iterable. '''

# Unpacking a list into variables 'a', 'b', and 'c' using the unpacking operator '*'
a, *b, c = [1, 2, 3, 4, 5]
# Explanation:
# - 'a' will capture the first element (1).
# - 'b' will capture all elements in the middle (2, 3, 4) as a list.
# - 'c' will capture the last element (5).
print(a)  # Output: 1
print(b)  # Output: [2, 3, 4]
print(c)  # Output: 5


# ------------------------- Merging Collections -----------------------------
''' This section demonstrates how to merge or concatenate multiple collections (lists, tuples, etc.) 
    using the unpacking operator `*`. This allows you to easily combine or join collections in a clean, readable way.'''

# Merging two lists using the unpacking operator '*'
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = [*list1, *list2]
# Explanation:
# - The `*` operator unpacks the elements of both 'list1' and 'list2' into a new list.
# - This effectively merges the two lists into a single collection.
print(merged_list)  # Output: [1, 2, 3, 4, 5, 6]


# ------------------------ Repeating Elements -----------------------------
''' This section demonstrates how to repeat elements within a collection using multiplication. 
    This feature works for both lists and tuples.'''

# Creating a list with repeated elements using the multiplication operator
zeros = [0] * 5
# Explanation:
# - The list `[0]` is multiplied by 5, resulting in a new list containing five 0s.
print(zeros)  # Output: [0, 0, 0, 0, 0]

# Creating a tuple with repeated elements using the multiplication operator
letters = ('a',) * 3
# Explanation:
# - The tuple ('a',) is repeated 3 times, resulting in a new tuple with three 'a' elements.
print(letters)  # Output: ('a', 'a', 'a')
