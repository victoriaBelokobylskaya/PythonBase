import json

profit = 0
avg_profit = 0
i = 0
dict_m = {}
try:
    with open("task_7.txt") as f_company:
        for line in f_company:
            list_company = list(line.split('\t'))
            list_company = [line.rstrip('\n') for line in list_company]
            profit = int(list_company[2]) - int(list_company[3])
            dict_t = {list_company[0]: profit}
            dict_m.update(dict_t)
            if profit > 0:
                avg_profit += profit
                i += 1
        avg_profit /= i
        dict_a = {"average_profit": avg_profit}
    itog = [dict_m,dict_a]
    print(itog)

    with open("task_7.json", "w", encoding="utf-8") as write_f:
        json.dump(itog, write_f)
except IOError:
    print("Ошибки при работе с файлом")