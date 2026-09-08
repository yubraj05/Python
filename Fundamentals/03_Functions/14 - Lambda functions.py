# Lambda functions in Python:
''' A lambda function is a small, anonymous function defined using the `lambda` keyword. 
    Lambda functions can take multiple parameters but only have a single expression that is evaluated and returned. '''

# Basic syntax: <variable> = lambda <parameters>: <expression>
# The variable now holds a reference to the lambda function, and calling this variable will execute the lambda function.

# Example 1: A lambda function that adds two numbers
add = lambda x, y: x + y  # 'x' and 'y' are parameters; the expression is 'x + y'
print(add(3, 5))  # Expected Output: 8
# Explanation: The lambda function takes two arguments, 'x' and 'y', and returns their sum.

# Example 2: A lambda function with a default argument (keyword argument)
add = lambda x, y=1: x + y  # 'x' is positional, and 'y' has a default value of 1
print(add(3))  # Expected Output: 6 because 'y' defaults to 1 when not provided
# Explanation: Here, the lambda function uses a default value for 'y'. When only 'x' is provided, 'y' defaults to 1.

# Example 3: A recursive lambda function to calculate the factorial of a number
factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)
print(factorial(5))  # Expected Output: 120
# Explanation: This lambda function computes the factorial of a number using recursion. 
# If 'n' is 0, it returns 1 (the base case), otherwise it multiplies 'n' by the result of factorial(n - 1).

# Example 4: A lambda function with no parameters (simple print statement)
say = lambda: print('Hello')  # A lambda function that takes no parameters and prints 'Hello'
say()  # Expected Output: Hello
# Explanation: This lambda function takes no parameters and simply prints 'Hello' when called.

