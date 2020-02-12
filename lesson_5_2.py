# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
num_s = 0
num_w = 0
try:
    with open("task_2.txt") as f_obj:
        for line in f_obj:
            num_s += 1
            line.strip()
            num_w = line.count(' ') + 1
            print(f"Строка: {num_s} кол-во слов: {num_w}")
    print(f"Всего строк: {num_s}")
except IOError:
    print("Не удалось открыть файл")
