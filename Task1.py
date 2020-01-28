class Matrix:
    def __init__(self, my_matrix):
        self.matrix = my_matrix

    def __str__(self):
        return 'Матрица:\n' + '\n'.join('\t'.join(map(str, line)) for line in self.matrix)

    def __add__(self, other):
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
                  for i in range(len(self.matrix))]
        return result


matrix_1 = [
    [31, 22],
    [-37, 43],
    [51, -86],
]

matrix_2 = [
    [30, 25],
    [23, -42],
    [15, 61],
]


a = Matrix(matrix_1)
print(a)
b = Matrix(matrix_2)
print(b)
c = Matrix(a + b)
print(c)
