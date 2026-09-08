functions = [lambda: i for i in range(5)]

# Calling each function
print([f() for f in functions])  # Output: [4, 4, 4, 4, 4] (unexpected)
