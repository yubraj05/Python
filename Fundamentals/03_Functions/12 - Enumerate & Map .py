# ENUMERATE FUNCTION
''' The enumerate() function adds a counter to an iterable and returns it as an enumerate object.
It is useful when you need both the index and the value from an iterable like a list. '''

my_list = ['apple', 'banana', 'cherry']

# Looping through the list using enumerate() to get both index and value
for index, value in enumerate(my_list):
    print(f"Index {index}: {value}")  # Output each item's index and value
    
# Example of using the start parameter in enumerate()
''' The start parameter allows you to specify the starting index for enumeration. By default, it starts at 0. '''
for index, value in enumerate(my_list, start=1):
    print(f"Item {index}: {value}")  # Outputs the item index starting from 1

# Expected output:
# Item 1: apple
# Item 2: banana
# Item 3: cherry


# MAP FUNCTION
''' The map() function applies a given function to each item in an iterable (like a list) and returns an iterable map object. 
It’s useful for transforming data in a list. '''

numbers = [1, 2, 3, 4, 5]

# Define a function to square a number
def square(x):
    return x ** 2

# Using map() to apply the square function to each element in the numbers list
squared_numbers = map(square, numbers)

# Convert the map object to a list to see the results
squared_numbers_list = list(squared_numbers)

print(squared_numbers_list)  # Expected output: [1, 4, 9, 16, 25]


# Using map() with a lambda function
''' Lambda functions are anonymous functions defined using the lambda keyword. They can be passed directly to map() 
for simple operations without the need to define a separate function. '''

numbers = [1, 2, 3, 4, 5]

# Using map() with a lambda function to square each number
squared_numbers = map(lambda x: x ** 2, numbers)

# Convert the map object to a list to see the results
squared_numbers_list = list(squared_numbers)

print(squared_numbers_list)  # Expected output: [1, 4, 9, 16, 25]
