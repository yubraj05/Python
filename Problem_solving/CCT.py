#                     ( CCT ---> Creative Critical Thinking )

# increment = lambda x, y=1: x + y
# print(increment(5))  # Output: 6

# a, b ,c = 4,(a:=3), 1  
# print(a,b,c) 


A = [1]
B = [0]
A.append(B) # 1stly B is appended to A that means list B is added to A    A = [1,[0]]

B.append(A) # But after this line everything changes completely
            # Now B  isn't just a list with element 0 but it's a list with referece to A 
# Previously A is also referenved to B that means it's in a infinite loop
# Now,
#  A = [1,[B]] 
#  B = [0,[A]] 

# Memory Representation of A:
# => A = [1, [0, A]]  
# => A = [1, [0, [1, B]]]  
# => A = [1, [0, [1, [0, A]]]]  
# => A = [1, [0, [1, [0, [1, [0, ...]]]]]] 

# Memory Representation of B:
# B = [0, [1, B]]
# B = [0, [1, [0, [1, B]]]]
# B = [0, [1, [0, [1, [0, [1, ...]]]]]]  # infinite loop!

print(A) 
print(B)




# ------------------------------- Solution ------------------------------------------


'''a = [1]
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
print(b)'''