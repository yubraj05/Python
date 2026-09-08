def mystery(a, b=[]):
    b.append(a)
    return b

x = mystery(10)  
y = mystery(20, [])  
z = mystery(30)  

print(x)  
print(y)  
print(z)  
