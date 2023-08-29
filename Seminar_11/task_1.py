# Создайте класс Матрица. 
# Добавьте методы для: вывода на печать, 
# сравнения, сложения, *умножения матриц


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])
       

    def __eq__(self, other):
        return self.matrix == other.matrix
    

    def __add__(self, other):
        result = [
            [self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
            for i in range(len(self.matrix))
        ]
        return Matrix(result)
    

    def __mul__(self, other):     
        result = [
            [
                sum(self.matrix[i][k] * other.matrix[k][j] for k in range(len(self.matrix[0])))
                for j in range(len(other.matrix[0]))
            ]
            for i in range(len(self.matrix))
        ]
        return Matrix(result)
    


m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])

print(m1 == m2, '\n')
print(m1 + m2, '\n')
print(m1 * m2, '\n')

