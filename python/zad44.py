def gauss(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) - 1

    for i in range(rows):
        pivot = matrix[i][i]
        for j in range(cols + 1):
            matrix[i][j] /= pivot
        for k in range(rows):
            if k != i:
                factor = matrix[k][i]
                for j in range(cols + 1):
                    matrix[k][j] -= factor * matrix[i][j]

    solutions = [row[cols] for row in matrix]

    return solutions


matrix1 = [
    [2, 1, -1, 8],
    [-3, -1, 2, -11],
    [-2, 1, 2, -3]
]

solution = gauss(matrix1)
print(solution)
