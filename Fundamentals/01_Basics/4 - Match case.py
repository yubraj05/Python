# This function demonstrates the use of Python's match-case statement for pattern matching.
# Pattern matching allows for more expressive and readable conditional logic.
# The function `describe_number` categorizes a number based on its value.

def describe_number(n):
    ''' Uses Python's match-case syntax to categorize a number into different types:
        - Negative number
        - Zero
        - Single-digit positive number
        - Double-digit or larger positive number '''
    
    match n:
        # Case 1: If the number is less than 0 (Negative number)
        case x if x < 0:
            return "Negative number"
        
        # Case 2: If the number is equal to 0
        case x if x == 0:
            return "Zero"
        
        # Case 3: If the number is a positive single-digit (between 1 and 9 inclusive)
        case x if 0 < x < 10:
            return "Single-digit positive number"
        
        # Case 4: If the number is 10 or larger (Double-digit or larger positive number)
        case x if x >= 10:
            return "Double-digit or larger positive number"

# Testing the function with different inputs
print(describe_number(-5))  # Expected Output: Negative number
print(describe_number(0))   # Expected Output: Zero
print(describe_number(5))   # Expected Output: Single-digit positive number
print(describe_number(10))  # Expected Output: Double-digit or larger positive number
