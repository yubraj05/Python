# Using filter with lambda function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using filter with a lambda function to filter even numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)

# Convert the filter object to a list to see the results
even_numbers_list = list(even_numbers)

print(even_numbers_list)  # Outputs: [2, 4, 6, 8, 10]


# Example of using zip
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
genders = ['Female', 'Male', 'Male']

# Using zip to combine elements from multiple lists
combined_data = zip(names, ages, genders)

# Convert the zip object to a list to see the results
combined_data_list = list(combined_data)

print(combined_data_list)
# Outputs: [('Alice', 25, 'Female'), ('Bob', 30, 'Male'), ('Charlie', 35, 'Male')]