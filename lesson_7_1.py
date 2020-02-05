from random import randint
import numpy as np

class Matrix():
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = [[i + randint(1, 10) * j + randint(0, 20) for j in range(m)] for i in range(n)]


    def __str__(self):
        total = ''
        for line in self.matrix:
            ln = str(line).strip('[]')
            total += f'{str(ln)}\n'
        return total

    def __add__(self, other):
        return np.array(self.matrix) + np.array(other.matrix)


my_m1 = Matrix(4, 4)
my_m2 = Matrix(4, 4)
print(f'Первая матрица:\n {my_m1}')
print(f'Вторая матрица:\n {my_m2}')

print(f'Результат сложения двух матриц:\n {my_m1 + my_m2}')
