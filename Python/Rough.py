#multiplication of matrices

a = [
[1,1,1],
[2,3,4],
[1,2,3]
]
b = [
[2,1,3],
[3,1,1],
[1,2,3]
]
l =[[0 for _ in range(3)] 
        for _ in range(3)
]


for i in range(3):
    for j in range(3):
        for k in range(3):
            l[j][i]+=a[j][k]*b[k][i]

for row in l:
    print(row)