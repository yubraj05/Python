# ------------------------ Local Scope -----------------------------
''' 
Local scope refers to variables that are defined within a function. These variables are accessible 
only inside the function where they are defined. 

Variables declared inside a function are local by default and cannot be accessed from outside the function.
'''

def my_function():
    x = 10  # Local variable 'x'
    print(x)  # Print the local variable 'x'

my_function()
# Uncommenting the next line will raise an error because 'x' is not accessible outside the function.
# print(x)  # Error: NameError: name 'x' is not defined outside of my_function


# ------------------------ Modifying Global Variables Inside Local Scope -----------------------------
''' 
You cannot modify a global variable inside a local scope (function) unless you explicitly declare it as 'global'. 
Without using the 'global' keyword, attempting to modify a global variable inside a function will result in an error.
'''

F = 10  # Global variable

def my_func():
    # Uncommenting the next line will raise an UnboundLocalError because 'F' is not declared locally.
    # F += 1  # Error: UnboundLocalError because 'F' is treated as a local variable

    global F  # Declare 'F' as global to modify the global variable inside the function
    F += 1  # This will modify the global variable 'F'

my_func()
print(F)  # Output: 11 (Global variable 'F' has been modified inside the function)


# ------------------------ Global Scope -----------------------------
''' 
Global scope refers to variables that are declared outside of any function. These variables can be accessed 
from anywhere in the code, both inside and outside functions.
'''

x = 10  # Global variable

def my_function():
    print(x)  # Accessing the global variable 'x' inside the function

my_function()
print(x)  # Accessing the global variable 'x' outside the function


# ------------------------ Nonlocal Scope -----------------------------
''' 
Nonlocal scope is used when working with nested functions. It allows you to modify a variable in the nearest 
enclosing scope (excluding the global scope). The 'nonlocal' keyword is used to refer to variables in the nearest 
enclosing scope and allows modifying them.

This is useful when you want to change a variable in the outer function from within an inner function.
'''

def outer_function():
    x = 10  # Variable in the outer function's local scope

    def inner_function():
        nonlocal x  # Declare that 'x' refers to the nearest enclosing scope (outer_function)
        x = 20  # Modify the variable in the outer function's scope

    inner_function()
    print("Outer function:", x)  # Output: Outer function: 20 (Modified by the inner function)

outer_function()

