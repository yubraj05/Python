#                     ( CCT ---> Creative Critical Thinking )

# increment = lambda x, y=1: x + y
# print(increment(5))  # Output: 6

# b ,c ,a= (a:=3), 1 ,2  
# print(b,c,a) 

'''a = [1]
b = [0]
a.append(b)
# [b] --> elements of b with []
# a --> elements of a without []
# a = [1,[b]] -- > [1,[0, a]] --> [1,[0,1,[b]]] --> [1,[0,[1,[0,a]]]] ...........
# here a is appended by b so brackets are included
b.extend(a)
# b = [0, a] --> b = [0,1,[b]] --> [0,1,[0, a]] --> [0,1[0,1,b]] ............
# here b is extended by a so brackets are not included
print(a)
print(b)'''

a = [1]
b = [0]
a.append(b[:])
# [b] --> elements of b with []
# a --> elements of a without []
# a = [1,[b]] -- > [1,[0, a]] --> [1,[0,1,[b]]] --> [1,[0,[1,[0,a]]]] ...........
# here a is appended by b so brackets are included
b.append(a[:])
# b = [0, a] --> b = [0,1,[b]] --> [0,1,[0, a]] --> [0,1[0,1,b]] ............
# here b is extended by a so brackets are not included
print(a)
print(b)