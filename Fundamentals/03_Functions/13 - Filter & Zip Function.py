# Using the filter() function with a lambda expression
''' The filter() function filters elements from an iterable based on a condition, and returns an iterator 
    containing only the elements for which the condition is True. A lambda function is used here as the condition. '''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using filter with a lambda function to filter even numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)  
# The lambda function checks if a number is divisible by 2 (i.e., even).

# Convert the filter object to a list to display the filtered results
even_numbers_list = list(even_numbers)

# Display the filtered list of even numbers
print(even_numbers_list)  # Expected Output: [2, 4, 6, 8, 10]

# Using zip() function to combine multiple iterables
''' The zip() function takes multiple iterables and aggregates them into tuples, pairing corresponding elements. 
    This is useful when you need to combine related data from multiple sequences. '''

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
genders = ['Female', 'Male', 'Male']

# Using zip to combine elements from multiple lists into a list of tuples
combined_data = zip(names, ages, genders)  
# This will create an iterator of tuples where each tuple contains one element from each iterable.

# Convert the zip object to a list to view the combined data
combined_data_list = list(combined_data)

# Display the combined list of tuples
print(combined_data_list)  
# Expected Output: [('Alice', 25, 'Female'), ('Bob', 30, 'Male'), ('Charlie', 35, 'Male')]
