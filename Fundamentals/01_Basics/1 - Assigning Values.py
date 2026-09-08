# Simple Assignment
''' In simple assignment, a variable is assigned a single value. '''
x = 5  # Assigning an integer to variable x
y = "Hello, World!"  # Assigning a string to variable y
z = [1, 2, 3]  # Assigning a list to variable z


# Multiple Assignments
''' In multiple assignment, multiple variables can be assigned values in a single statement. '''
a, b, c = 1, 2, 3  # Assigning 1 to a, 2 to b, and 3 to c simultaneously


# Chained Assignment
''' Chained assignment allows the same value to be assigned to multiple variables at once. '''
x = y = z = 0  # All three variables (x, y, z) are assigned the value 0


# Unpacking Assignments
''' Unpacking allows you to extract elements from iterables (like lists or tuples) and assign them to variables. '''

a, b, c = (1, 2, 3)  # Unpacking a tuple (1, 2, 3) into variables a, b, and c

x, y, z = [4, 5, 6]  # Unpacking a list [4, 5, 6] into variables x, y, and z

p, q, r = "abc"  # Unpacking a string "abc" into variables p, q, and r


# Unpacking with the Asterisk (*)
''' The asterisk (*) is used to collect multiple values into a list, known as "star unpacking".'''

a, *b, c = [1, 2, 3, 4, 5]  
# a = 1, b = [2, 3, 4], c = 5; "b" collects all elements between a and c into a list.

*start, end = [10, 20, 30, 40]  
# start = [10, 20, 30], end = 40; "start" collects all values except the last one.

first, *middle, last = [7, 8, 9, 10]  
# first = 7, middle = [8, 9], last = 10; "middle" collects the values in between.

 
# Ignoring Values
''' You can use the underscore (_) to ignore specific values during unpacking.'''

a, _, b = (1, 2, 3)  
# a = 1, b = 3; the underscore (_) is used to ignore the second value (2).

first, *_, last = [10, 20, 30, 40, 50]  
# first = 10, last = 50; the asterisk (*) collects values in the middle, which are ignored using "_".

 
# Swapping Values
''' Swapping values allows you to exchange the values of two variables in a single operation. '''

a, b = 5, 10  # Assign 5 to a, and 10 to b
a, b = b, a  # Swap values; a becomes 10, and b becomes 5


# Assigning Values in Data Structures
''' You can assign or modify values in data structures like lists, dictionaries, and sets. '''

# List Assignment
my_list = [1, 2, 3]  # Assign a list to my_list
my_list[0] = 10  # Modify the first element of the list to 10, resulting in [10, 2, 3]

# Dictionary Assignment
my_dict = {'a': 1, 'b': 2}  # Create a dictionary with key-value pairs
my_dict['a'] = 10  # Modify the value associated with key 'a' to 10, resulting in {'a': 10, 'b': 2}

# Set Assignment
my_set = {1, 2, 3}  # Assign a set to my_set
my_set.add(4)  # Add the element 4 to the set, resulting in {1, 2, 3, 4}


# Using exec for Dynamic Assignment
''' The exec function allows dynamic execution of Python code, including assignments.'''

expr = "x = 5"  # Assign the expression as a string
exec(expr)  # Executes the expression, assigning 5 to x
print(x)  # Output: 5; x is now 5 because exec executed the assignment.

# Using eval for Dynamic Assignment
''' The eval function evaluates a string as a Python expression and returns the result.'''

expr = "4 + 5"  # Define a mathematical expression as a string
expr = eval(expr)  # Evaluate the expression, resulting in 9
print(expr)  # Output: 9; eval evaluates the string and returns the result.
