from math import factorial


def func_gen(n):
    for el in range(1, n + 1):
        yield el


# n = 10
k = 5
i = 1
try:
    n = int(input('Введите n: '))
    for el in func_gen(n):
        if i <= k:
            f = factorial(el)
            print(f)
            i += 1
        else:
            print('Конец работы')
            break
except ValueError:
    print('Введено не корректное значение n')
