
''' Decorators in Python are a design pattern that allows you to add new 
    functionality to an existing object without modifying its structure.'''

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

@run_time
def for_fact(num):
    'Factorial using for loop '
    if num == 0:
        return 1
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

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
    print("Hello")
hello()
print(for_fact(10))
print(while_fact(10))

