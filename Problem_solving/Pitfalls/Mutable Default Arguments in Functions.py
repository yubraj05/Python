def add_item(item, lst=[]):
    lst.append(item)
    return lst

print(add_item(1))  # Output: [1]
print(add_item(2))  # Output: [1, 2] (Unexpected!)

#Corrected
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

# Corrected
def add_item(item):
    lst = []
    lst.append(item)
    return lst
