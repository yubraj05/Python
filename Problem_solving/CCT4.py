# Add two Matrices 

#Using Comprehension

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]
result = [
    [matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))]
    for i in range(len(matrix1))
]

for row in result:
    print(row)


# Without using Comprehension

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Initialize the result matrix with zeros
rows = len(matrix1)
cols = len(matrix1[0])
result = [[0 for _ in range(cols)] for _ in range(rows)]

# Add the matrices
for i in range(rows):
    for j in range(cols):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

# Print the result
for row in result:
    print(row)