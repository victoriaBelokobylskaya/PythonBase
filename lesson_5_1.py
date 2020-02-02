# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# # Об окончании ввода данных свидетельствует пустая строка.

f_obj = open("task_1.txt", "w")
f_obj.close()
try:

    with open("task_1.txt", "a") as f_obj:
        while True:
            content = input("Введите строку, завершение ввода - пустая строка: ")
            if not content:
                break
            else:
                content += "\n"
                f_obj.write(content)

            if not content:
                break
except IOError:
    print("Ошибка при открытии/закрытии файла")