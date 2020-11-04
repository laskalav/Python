class OrganicCell(object):
    def __init__(self, sum_cell):
        self.sum_cell = sum_cell

    def __add__(self, other):
        sum = self.sum_cell + other.sum_cell
        return OrganicCell(sum_cell=sum)

    def __sub__(self, other):
        diff = self.sum_cell - other.sum_cell
        if diff > 0:
            return OrganicCell(sum_cell=diff)
        else:
            print("Клетки больше нет")

    def __mul__(self, other):
        multiply = self.sum_cell * other.sum_cell
        return OrganicCell(sum_cell=multiply)

    def __truediv__(self, other):
        div = self.sum_cell * other.sum_cell
        return OrganicCell(sum_cell=int(div))

    def make_order(self, row):
        ful_cells = self.sum_cell // row
        cells_remaining = self.sum_cell % row
        result = '\n'.join(['*' * row] * ful_cells) + '\n' + '*' * cells_remaining
        return result


