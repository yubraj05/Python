# KEY CONCEPT
''' A decorator is a function that takes another function as an argument and returns a new function 
that typically extends or modifies the behavior of the original function without altering its core implementation.'''

# What happens behind the scenes:
''' In simple terms, if you need to modify a function's behavior without changing the function itself, 
a decorator provides an elegant solution.'''

''' 1. A decorator is essentially a function that contains a nested function. The outer function 
takes the original function as an argument and the inner function (the "wrapper") handles the additional logic.'''

# def decor(func):                 
#     def wrapper(name): 
#         print("Before function execution")  # Code that runs before the original function
#         result = func(name)  # Call the original function
#         print("After function execution")  # Code that runs after the original function
#         return result  # Return the result of the original function
#     return wrapper  # The decorator returns the modified version of the original function

# def greet(name):
#     return f"Hello, {name}"

''' 2. To understand how it works, think of the decorator as a wrapper around the original function. 
If we call the decorator like this:'''

# res = decor(greet)  # The 'greet' function is passed to the decorator, and it returns the modified function (wrapper)

''' 3. The decorator returns the wrapper function, which now incorporates additional behavior. 
At this point, the function `res` behaves like the wrapper, how?, let’s see this through an example:'''

# def greet(name):
#     return f"Hello, {name}"
# res = greet  # This simply refers to the original greet function
# print(res('Yubraj'))  # Calls the original greet function and outputs "Hello Yubraj"

''' 4. To make things clearer, let's explore what happens when the wrapper is called:'''

# output = res('Yubraj')  # When `res` (the wrapper function) is invoked, it adds extra behavior around the original greet function

''' 5. The wrapper function executes the additional code and then calls the original function. 
Instead of manually calling the wrapper, we can apply the decorator directly to the function like this:'''

# greet = decor(greet)  # The original greet function is now wrapped by the decorator

''' 6. Now, when we call the decorated greet function, it will still behave as the original function, but with added functionality.'''

# print(greet("Yubraj"))  # This will print "Before function execution", then "Hello Yubraj", and finally "After function execution"










#----------------------------------------------------------------------------------------------------------------------







# CODE STARTS FROM HERE

import time 

#creating the decorator
def run_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Time required for {func.__doc__}: {end_time - start_time:.6f} seconds")
        return result
    return wrapper


# for_fact = run_time(for_fact) >manually using decorator
# for_fact()
@run_time
def for_fact(num):
    'Factorial using for loop '
    if num == 0:
        return 1
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

for_fact = run_time(for_fact)
print(for_fact(4))

# while_fact = run_time(while_fact) >manually using decorator
# while_fact()
@run_time
def while_fact(num):
    'Factorial using while loop '
    if num == 0:
        return 1
    result = 1
    i = 1
    while i<=num:
        result*=i
        i+=1
    return result
    
@run_time
def hello():
    'greet'
    print("Hello")

hello()
print(for_fact(10))
print(while_fact(10))

