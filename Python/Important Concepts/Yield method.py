def rep(a):
    for i in range(a):
        yield i


x = list(rep(10))
y = list(range(10))
print(*x , *y )