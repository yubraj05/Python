a,b = 10,8
def show(res):
    print(f"{a:b}",a,sep=" ")
    print(f"{b:b}",b)
    print('--------')
    print(f"{res:b}",res)

AND = a & b
OR = a | b
NOT = ~a
XOR = a ^ b


show(AND)
# show(OR)
# show(NOT)
# show(XOR)
