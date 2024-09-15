# dict1 = {}
# for i in range(1,11):
#     dict1[i] = i*2

# dict1 = {i:i*2 for i in range(1,11)}
# print(dict1)


# dict1 = {i:i*2 for i in range(1,11) if i%2==0} #cant use else here directly
# print(dict1)

# dict1 = {i:i*2 if i%2==0 else i+1 for i in range(1,11)} #right syntex for using else 
# print(dict1)


# dict1 = {n:{i:i*2 if i%2==0 else i+1 for i in range(1,6)} for n in range(5)}
# print(dict1)

name = 'jubraj'
charcount = {char:name.count(char) for char in name}
print(list(charcount.values()))