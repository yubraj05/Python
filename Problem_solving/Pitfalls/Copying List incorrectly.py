a = [1, 2, 3]
b = a  # Both refer to the same object
b.append(4)
print(a)  # Output: [1, 2, 3, 4] (Unexpected!)

a = [1, 2, 3]
b = a[:] 
b.append(4) 
print(a)        # Slicing
b = list(a) 
b.append(4)   
print(a)   # Using list()
b = a.copy()   
b.append(4)
print(a)   # Using .copy()

