# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

my_list = list(input('Введите список: '))

if len(my_list) % 2 == 0:
    my_list[::2], my_list[1::2] = my_list[1::2], my_list[::2]
else:
    temp = my_list.pop()
    my_list[::2], my_list[1::2] = my_list[1::2], my_list[::2]
    my_list.append(temp)

print(my_list)

