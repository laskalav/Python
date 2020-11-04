from copy import copy


class Matrix(object):
    def __init__(self, matrix):
        if isinstance(matrix, list):
            for index, el in enumerate(matrix):
                if not isinstance(el, list):
                    raise TypeError
                if len(el) != len(matrix[index - 1]):
                    raise Exception("Длина вложенных списков не совпадает!")

        self.matrix = matrix

    def __str__(self) -> str:
        return str(self.matrix)

    def __repr__(self) -> str:
        [str(i) for i in self.matrix]
        return "\n".join([str(i) for i in self.matrix])

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise Exception("слагаемое не экземпляр класса Matrix!")
        if self.shape != other.shape:
            raise Exception("Форма матриц разная!")
        new_matrix = copy(self)
        for x, row in enumerate(other.matrix):
            for y, el in enumerate(row):
                new_matrix.matrix[x][y] = self.matrix[x][y] + other.matrix[x][y]
        return new_matrix


    @property
    def shape(self):
        row = len(self.matrix)
        column = len(self.matrix[0])
        return row, column


if __name__ == '__main__':
    matrix1 = Matrix(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matrix2 = Matrix(matrix=[[9, 8, 7],[6, 5, 4],[3, 2, 1]])
    print(repr(matrix1 + matrix2))
