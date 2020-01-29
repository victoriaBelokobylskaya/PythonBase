# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.


f_new = open("task_4_new.txt", "w", encoding="utf-8")
f_new.close()
rus_w = ['Один', 'Два', 'Три', 'Четыре']
i = 0
new_cont = ''
try:
    with open("task_4.txt") as f_obj:
        for content in f_obj:
            word = (content[:(content.index('—') - 1)])
            new_cont = content.replace(word, rus_w[i])
            with open("task_4_new.txt", "a") as f_new:
                f_new.write(new_cont)
            i += 1
except IOError:
    print("Ошибка открытия файла")
