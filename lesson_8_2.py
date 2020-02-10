# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых
# пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
# завершиться с ошибкой.

class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt

input_n1 = int(input("Введите делимое: "))
input_n2 = int(input("Введите делитель: "))

try:
    if input_n2 == 0:
        raise MyError("Вы ввели ноль!")
except ValueError:
    print("Вы ввели не число")
except MyError as err:
    print(err)
else:
    print(f"Частное {input_n1} / {input_n2} = {input_n1 / input_n2 }")
finally:
    print('Конец!')