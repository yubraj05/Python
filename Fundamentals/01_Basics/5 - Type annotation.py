# Type Hinting in Python
''' This code demonstrates how to use type hinting in Python to specify the expected data types of variables and function parameters/returns. '''

# Variable declaration with type hinting
age = '5'  # age is currently a string, but we expect it to be an integer
age: int  # Type hint indicating that the 'age' variable should be of type 'int'
# Note: Python will not enforce this type at runtime. Type hints are for readability, documentation, and static analysis tools.

name: str = "Alice"  # Type hint specifying that 'name' is expected to be a string

# Printing the type of the 'age' variable to demonstrate the current type
print(type(age))  # Output: <class 'str'> because 'age' is assigned a string value '5'

# Function with type hinting for parameters and return value
def greet(name: str) -> str:
    ''' This function takes a string as input (name) and returns a greeting message as a string. '''
    return f"Hello, {name}"

# Function with type hinting for parameters and return value
def add(a: int, b: int) -> int:
    ''' This function takes two integers as input (a, b) and returns their sum as an integer. '''
    return a + b

# If a function is called with an unexpected value, it will raise an error during execution
# Python does not enforce type hints at runtime, but if types do not match the expected ones, the code may fail in certain situations.

# Example:
# Uncommenting the following line would result in a runtime error due to incompatible types
# print(add('5', 10))  # Raises TypeError since '5' is a string, not an integer

