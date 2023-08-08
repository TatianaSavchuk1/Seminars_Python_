# Напишите функцию для транспонирования матрицы 
# Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]

def transpose_matrix (matrix_1):

    matrix_2 = []

    zip_rows = zip(*matrix_1)

    matrix_2 = [list(row) for row in zip_rows]
    return matrix_2


matrix = [[1, 2, 3], [4, 5, 6]]
print(transpose_matrix(matrix))