lst = [[i for i in range(1,6)] for l in range(3)]
print(lst)

lst1 = [[i+m for i in range(1,4)] for m in range(3)]
print(lst1)

flat_list = [item for sublist in lst1 for item in sublist]
print(flat_list)