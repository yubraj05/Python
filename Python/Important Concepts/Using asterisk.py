# Unpacking in Assignments
a, *b, c = [1, 2, 3, 4, 5]
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5

# Merging Collections
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = [*list1, *list2]

print(merged_list)  # [1, 2, 3, 4, 5, 6]

# Repeating Elements
zeros = [0] * 5
print(zeros)  # [0, 0, 0, 0, 0]

letters = ('a',) * 3
print(letters)  # ('a', 'a', 'a')

