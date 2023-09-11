import logging

logging.basicConfig(filename='log_file.log', encoding='utf-8', filemode='a', level=logging.INFO)
logger = logging.getLogger(__name__)

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])
       

    def __eq__(self, other):
        try:
            self.matrix == other.matrix
            logging.info(f'сравнили матрицы {self.matrix} и {other.matrix}')
        except Exception as ex:
            logging.error(f'Возникла такая ошибка: {ex}')
    

    def __add__(self, other):
        try:
            result = [
                [self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
                for i in range(len(self.matrix))
            ]
            logging.info( Matrix(result))
        except Exception as ex:
            logging.error(f'Возникла такая ошибка: {ex}')

    def __mul__(self, other):     
        try:
            result = [
                [
                    sum(self.matrix[i][k] * other.matrix[k][j] for k in range(len(self.matrix[0])))
                    for j in range(len(other.matrix[0]))
                ]
                for i in range(len(self.matrix))
            ]
            logging.info (Matrix(result))
        except Exception as ex:
            logging.error(f'Возникла такая ошибка: {ex}')


m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])

print(m1 == m2, '\n')
print(m1 + m2, '\n')
print(m1 * m2, '\n')
