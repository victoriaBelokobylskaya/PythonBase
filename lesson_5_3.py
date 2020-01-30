# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32
sum_usr = 0.00
total_s = 0.00
count = 0
try:
    with open("task_3.txt") as f_obj:
        for content in f_obj:
            sum_usr = float(content[(content.index(' ') + 1):])
            if sum_usr < 20000:
                print(content[:content.index(' ')], sum_usr)
            total_s += sum_usr
            count += 1
except IOError:
    print('Не удалось открыть/закрыть файл')
print(f'Средняя ЗП: {total_s / count} сотрудников {count}')
