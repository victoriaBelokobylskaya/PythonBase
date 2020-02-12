class DigitlError(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []

while True:
    try:
        num = input('Введите число. Завершение ввода - пустая строка ')
        if not num:
            break
        else:
            if num.isdigit():
                my_list.append(num)
            else:
                raise DigitlError("Введено не число")
    except DigitlError as my_err:
        print(my_err)
    if not num:
        break

print(my_list)