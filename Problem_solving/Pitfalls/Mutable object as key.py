# d = {}
# key = [1, 2, 3]  # Lists are mutable
# d[key] = "value"  # TypeError: unhashable type: 'list'

d = {}
key = 1  # Lists are mutable
d[key] = "value"  # TypeError: unhashable type: 'list'
print(d)