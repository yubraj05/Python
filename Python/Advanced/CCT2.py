# Reference

a = [1,[2,3],4]
b = a[1]    # here a reference is created from the list a 
a.pop(1)    # the list '[2,3]' is removed only from the refernce of a

# The reference is removed but the list is still at same location in memory
print(b)

# The item exists as long as its referenced
