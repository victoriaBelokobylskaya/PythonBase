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
        a = np.self.matrix
        b = np.other.matrix
        return a + b


my_m1 = Matrix(5, 6)
print(my_m)

my_m2 = Matrix(5,6)
print(my_m1 + my_m2)
