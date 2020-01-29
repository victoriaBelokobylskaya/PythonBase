# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randint
count = 0
try:
    with open("task_5.txt", "w") as f_obj:
        f_obj.writelines(' '.join([str(randint(1, 100)) for _ in range(1, 10)]))
except IOError:
    print('Ошибка открытия, закрытия файла')

try:
    with open("task_5.txt", "r") as f_obj:
        for line in f_obj:
            my_list = list(line.split(" "))
            print(my_list)
            for el in my_list:
                if not el:
                    break
                else:
                    count += int(el)
            print(count)
except IOError:
    print('Ошибка открытия, закрытия файла')