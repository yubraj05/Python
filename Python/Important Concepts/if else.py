#result = value_if_true if condition else value_if_false

def describe_number(n):
    match n:
        case x if x < 0:
            return "Negative number"
        case x if x == 0:
            return "Zero"
        case x if 0 < x < 10:
            return "Single-digit positive number"
        case x if x >= 10:
            return "Double-digit or larger positive number"

print(describe_number(-5))  # Output: Negative number
print(describe_number(0))   # Output: Zero
print(describe_number(5))   # Output: Single-digit positive number
print(describe_number(10))  # Output: Double-digit or larger positive number