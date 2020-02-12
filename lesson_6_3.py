# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
# (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker():
    def __init__(self, name, surname, position, profit, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"profit": profit, "bonus": bonus}
        # self._income = income # словарь
        # for key in income:
        #     setattr(self, key, income[key])


class Position(Worker):
    def __init__(self, name, surname, position, profit, bonus):
        super().__init__(name, surname, position, profit, bonus)

    def get_full_name(self):
        print(f'ФИО: {self.name} {self.surname}')

    # нужно посчитать доход оклад + бонус
    def get_total_income(self):
        itog = 0
        for i in self._income.values():
            itog += int(i)
        print(f'Итоговый доход: {itog}')


man_1 = Position('Max', 'Plank', 'CEO', 1000, 500)
man_1.get_full_name()
man_1.get_total_income()
