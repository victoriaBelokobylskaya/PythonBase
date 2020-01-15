# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

num = int(input("Введите чило: "))

temp = 0
max_n = 0

while num > 1:
    if max_n < temp:
        max_n = temp
    temp = num % 10
    num //= 10

if max_n < temp:
    max_n = temp

print(max_n)
