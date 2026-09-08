#---------------------------- Unpacking Function Arguments -------------------------
''' This section demonstrates how to unpack arguments when calling a function using the 
    unpacking operators `*` for positional arguments and `**` for keyword arguments. '''

# Function that takes three parameters
def foo(a, b, c):
    print(a, b, c)

# Example with positional argument unpacking
args = (1, 2, 3)  # Tuple with values to unpack into 'a', 'b', and 'c'
foo(*args)  # Unpacks the tuple and calls foo(1, 2, 3)
# Output: 1 2 3

# Example with keyword argument unpacking
kwargs = {'a': 1, 'b': 2, 'c': 3}  # Dictionary with key-value pairs to unpack into keyword arguments
foo(**kwargs)  # Unpacks the dictionary and calls foo(a=1, b=2, c=3)
# Output: 1 2 3


#------------------------ Variable-Length Argument Lists ------------------------
''' This section demonstrates the use of variable-length argument lists, allowing 
    functions to accept an arbitrary number of positional arguments and keyword arguments. '''

# Function that accepts both positional and keyword arguments
def foo(*args, **kwargs):
    print("Positional arguments:", args)  # 'args' will be a tuple of all positional arguments
    print("Keyword arguments:", kwargs)  # 'kwargs' will be a dictionary of all keyword arguments

# Call the function with a mix of positional and keyword arguments
foo(1, 2, 3, a=4, b=5)  
# Output: 
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'a': 4, 'b': 5}


#------------------------- Keyword-Only Arguments -----------------------------
''' This section demonstrates the use of keyword-only arguments, which are specified 
    after a `*` in the function definition, ensuring that they can only be passed by keyword. '''

# Function with keyword-only argument 'c'
def foo(a, b, *, c):
    print(a, b, c)

# Valid call with keyword-only argument 'c'
foo(1, 2, c=3)  # Must specify 'c' as a keyword argument
# Output: 1 2 3

# Invalid call (uncommenting this will raise a TypeError)
# foo(1, 2, 3)  # Error: 'c' must be specified as a keyword argument after the '*'
# Explanation: After declaring '*' in the function signature, all arguments after it must be passed as keyword arguments.
