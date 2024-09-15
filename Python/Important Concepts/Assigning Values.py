# Simple Assignment
x = 5
y = "Hello, World!"
z = [1, 2, 3]


# Multiple Assignments
a, b, c = 1, 2, 3


# Chained Assignment
x = y = z = 0


#  Unpacking Assignments
a, b, c = (1, 2, 3) # Unpacking a tuple

x, y, z = [4, 5, 6] # Unpacking a list

p, q, r = "abc" # Unpacking with a mix of values


# Unpacking with the Asterisk (*)
a, *b, c = [1, 2, 3, 4, 5]  # a = 1, b = [2, 3, 4], c = 5

*start, end = [10, 20, 30, 40]  # start = [10, 20, 30], end = 40

first, *middle, last = [7, 8, 9, 10] # first = 7, middle = [8, 9], last = 10


# Ignoring Values
a, _, b = (1, 2, 3) # a = 1, b = 3

first, *_, last = [10, 20, 30, 40, 50] # first = 10, last = 50


# Swapping Values
a, b = 5, 10
a, b = b, a # a = 10, b = 5


# Assigning Values in Data Structures

# List
my_list = [1, 2, 3]
my_list[0] = 10  # [10, 2, 3]

# Dictionary
my_dict = {'a': 1, 'b': 2}
my_dict['a'] = 10  # {'a': 10, 'b': 2}

# Set
my_set = {1, 2, 3}
my_set.add(4)  # {1, 2, 3, 4}


# Using exec for Dynamic Assignment

expr = "x = 5"
exec(expr)
print(x)  # 5

# Using eval for Dynamic Assignment

expr = "4+5"
expr = eval(expr)
print(expr)  # 5