class Cell:
    def __init__(self, count_cells):
        self.count_cells = count_cells

    def __str__(self):
        return f"{self.count_cells}"

    def __add__(self, other):
        return Cell(self.count_cells + other.count_cells)

    def __sub__(self, other):
        if self.count_cells - other.count_cells > 0:
            return self.count_cells - other.count_cells
        else:
            return f'Разность меньше 0'

    def __mul__(self, other):
        return Cell(self.count_cells * other.count_cells)

    def __truediv__(self, other):
        if self.count_cells / other.count_cells > 1:
            return f'{(self.count_cells / other.count_cells):0.2f}'
        else:
            return f'Частное меньше 0'

    def make_order(self, num):
        i = 1
        total = ''
        while i <= self.count_cells // num:
            i += 1
            total += f"{num * '*'}\n"
        num = self.count_cells % num
        total += f"{num * '*'}\n"
        return total

# проверка метода make_order
# my_cell_1 = Cell(6)
# my_cell_2 = Cell(80)
# print(my_cell_2.make_order(7))

my_cell_1 = Cell(6)
my_cell_2 = Cell(4)
print(my_cell_1 + my_cell_2)

print(my_cell_1 - my_cell_2)
print(my_cell_2 - my_cell_1)

print(my_cell_1 * my_cell_2)

print(my_cell_1 / my_cell_2)
print(my_cell_2 / my_cell_1)
