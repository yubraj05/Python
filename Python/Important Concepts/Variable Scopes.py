# Local Scope
'''Local scope refers to variables defined within a function. 
These variables are accessible only within the function where they are defined.

Variables declared inside a function are local by default.
They cannot be accessed or modified from outside the function.
Example of local scope:'''

def my_function():
    x = 10  # Local variable
    print(x)

my_function()
# print(x)  # Error: x is not defined outside my_function



# NOTE: YOU CANNON MODIFY THE GLOBAL VARIABLE INSIDE LOCAL SCOPE IE INSIDE FUNCTION
F = 10
def my_func():
    # F+=1 
    # It will raise an UnboundLocalError because F isnt declared inside the local scope 
    global F 
    F+=1
my_func()
print(F)





#  Global Scope
'''Global scope refers to variables defined outside of any function or declared as global within a function. These variables can be accessed from anywhere within the code.

Variables declared outside all functions are global by default.
Global variables can be accessed and modified from any part of the program.
Example of global scope:'''

x = 10  # Global variable

def my_function():
    print(x)  # Accessing global variable inside function

my_function()
print(x)  # Accessing global variable outside function




# Nonlocal Scope
'''Nonlocal scope is a special scope used inside nested functions. It allows you to modify a variable in the nearest enclosing scope (excluding global scope).

Used when you want to modify a variable in an outer (enclosing) function from within an inner nested function.
The nonlocal keyword is used to declare a variable as nonlocal.
Example of nonlocal scope:'''


def outer_function():
    x = 10  # Outer function's local variable

    def inner_function():
        nonlocal x
        x = 20  # Modifying the outer function's variable

    inner_function()
    print("Outer function:", x)  # Prints the modified value

outer_function()