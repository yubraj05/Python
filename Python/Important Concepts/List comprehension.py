list1 = [1,3,4,5,6,7,8]
list2 = []
# for i in list1:
#     if i%2==0:
#         list2.append(i)
#     else:
#         list2.append(i+1)
# print(list2)
list2 = [i if i%2==0 else i+1 for i in list1 ]


print(*list2)

