from sys import argv

try:
    script_name, hours, cost_h, bonus = argv


    def salary(hours, cost_h, bonus):
        return hours * cost_h + bonus

    print(salary(int(hours), int(cost_h), int(bonus)))
except ValueError:
    print('Проверьте ввод параметров')
