# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(v_1, v_2, v_3):
    my_list = list(str(v_1 + v_2 + v_3))
    my_list.sort(reverse=True)
    my_list.pop()

    return int(my_list[0]) + int(my_list[1])


print(my_func(v_1=input('Первое число: '), v_2=input('Второе число: '), v_3=input('Третье число: ')))
