ch = ''
count = 0
dict_t = {}
dict_m ={}

try:
    with open("task_6.txt") as f_txt:
        for line in f_txt:
            my_list = list(line.split(' '))
            print(my_list)
            ch = ''
            count = 0
            for el in my_list:
                ch = ''
                for i in filter(str.isdigit, str(el)):
                    if not i:
                        break
                    else:
                        ch += i
                if ch.isdigit():
                    count += int(ch)
            dict_t = {my_list[0]: count}
            dict_m.update(dict_t)
    print(f'\n Итоговый словарь: {dict_m}')
except IOError:
    print("Не удалось открыть/закрыть файл")