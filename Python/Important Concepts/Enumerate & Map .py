# ENUMERATE FUNCTION
my_list = ['apple', 'banana', 'cherry']

for index, value in enumerate(my_list):
    print(f"Index {index}: {value}")
    
# Example with start parameter
for index, value in enumerate(my_list, start=1):
    print(f"Item {index}: {value}")

# Outputs:
# Item 1: apple
# Item 2: banana
# Item 3: cherry


# MAP FUNCTION
numbers = [1, 2, 3, 4, 5]

# Define a function to square a number
def square(x):
    return x ** 2

# Using map to square each number in the list
squared_numbers = map(square, numbers)

# Convert the map object to a list to see the results
squared_numbers_list = list(squared_numbers)

print(squared_numbers_list)  # Outputs: [1, 4, 9, 16, 25]


# Using map with lambda function
numbers = [1, 2, 3, 4, 5]

# Using map with a lambda function to square each number
squared_numbers = map(lambda x: x ** 2, numbers)

# Convert the map object to a list to see the results
squared_numbers_list = list(squared_numbers)

print(squared_numbers_list)  # Outputs: [1, 4, 9, 16, 25]