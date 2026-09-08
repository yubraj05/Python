a = 256
b = 256
print(a is b)  # Output: True (due to integer caching)
c = 257
d = 257
print(c is d)  # Output: False (Python only caches integers from -5 to 256)


print(a == b)  # Output: True
print(c == d)  # Output: True
