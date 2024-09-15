#Determinant 

def get_cofactor(matrix, p, q, n):
    cofactor = []
    for i in range(n):
        row = []
        for j in range(n):
            if i != p and j != q:
                row.append(matrix[i][j])
        if row:
            cofactor.append(row)
    return cofactor

def determinant(matrix, n):
    if n == 1:
        return matrix[0][0]
    
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for i in range(n):
        cofactor_matrix = get_cofactor(matrix, 0, i, n)
        det += ((-1) ** i) * matrix[0][i] * determinant(cofactor_matrix, n - 1)
    
    return det


matrix_3x3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = len(matrix_3x3)
det = determinant(matrix_3x3, n)

print(f"Determinant of the 3x3 matrix: {det}")