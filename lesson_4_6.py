from my_cycle import new_cycle
from my_count import new_count

while True:
    try:
        mode = int(input('Выберете режим работы скрипта \n Функция count - 1 \n Функция cycle - 2 \n Выход - 3 \n Ваш выбор: '))
        if mode == 1:
            print(new_count(s=int(input('Введите стартовое значение: ')), e=int(input('Введите окончание: '))))
        elif mode == 2:
            print(new_cycle(l=(input('Введите набор слов: ').split(' ')), c=int(input('Введите количество повторений: '))))
        elif mode == 3:
            print('Конец работы скрипта')
            break
        else:
            print('\n Такого режима не существует')
    except ValueError:
        print('\n Введены не корректные значения')
