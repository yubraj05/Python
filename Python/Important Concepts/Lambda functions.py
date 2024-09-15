#<variable> = lambda [Parameters] : [Expression]
# The variable is now the function object 
# The variable has the return value as lambda function returns the [Expression] directly

# Example of a lambda function that adds two numbers
add = lambda x, y: x + y # x,y are parameters 
print(add(3, 5))  # Outputs: 8

add = lambda x, y=1 : x + y # x is positional while y is keyword
print(add(3))  # Outputs: 6 bcz y = 1 by default

factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)
print(factorial(5))

say = lambda : print('Hello')
say()

