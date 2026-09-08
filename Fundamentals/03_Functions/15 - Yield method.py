# -------------------- Using a Generator Function with 'yield' ------------------------
''' 
A generator function allows you to iterate over data without storing the entire dataset in memory at once. 
This is achieved by using the 'yield' keyword, which returns an item at a time and suspends the function's execution 
until the next item is requested. 

In this example, we use a generator function 'rep' to generate a sequence of numbers from 0 to 'a-1'.
'''

def rep(a):
    for i in range(a):
        yield i  # 'yield' generates each number in the range, one at a time

# Generate a list of numbers from 0 to 9 using the 'rep' generator function
x = list(rep(10))  # Convert the generator to a list

# Generate the same list using the built-in range function
y = list(range(10))  # Convert the range object to a list

# Print both lists side by side
print(*x, *y)  # The '*' operator unpacks both lists into the print function
