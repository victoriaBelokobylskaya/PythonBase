class DigitlError(Exception):
    def __init__(self, txt):
        self.txt = txt

class Warehouse():
    def __init__(self, title):
        self.new_eq = {}
        self.from_wr = []
        self.title = title

    def num_w(self):
        print(f'Склад номер {self.title}')

    # прием оборудования на склад
    @classmethod
    def get_eq(cls, *eq):
        cls.new_eq = list(eq)
        return f'На склад получено {cls.new_eq}'

    # отпрвка оборудования на склад
    def send_eq(self, *wr):
        self.from_wr = list(wr)
        return f'Со склада отправлено {self.from_wr}'

class OffEquipment(Warehouse):
    """ Ввод инфо об оборудовании тип, модель, функция, кол-во, цена """

    def __init__(self, title, type_e, model, func, count, cost):
        super().__init__(title)
        self.info = {"Тип оборудования": type_e, "Модель": model, "Функция": func, "Количество": count, "Цена": cost}

    def __str__(self):
        return str(self.info)


class Printer(OffEquipment):
    def __init__(self, title, type_e, model, func, count, cost):
        super().__init__(title, type_e, model, func, count, cost)

    def add_print_info(self, double_print, tech):
        self.info.update({"Двусторонняя печать": double_print})
        self.info.update({"Технология печати": tech})


class Scan(OffEquipment):
    def __init__(self, title, type_e, model, func, count, cost):
        super().__init__(title, type_e, model, func, count, cost)

    def add_scan_info(self, max_format):
        self.info.update({"Максимальный формат бумаги": max_format})


class Xerox(OffEquipment):
    def __init__(self, title, type_e, model, func, count, cost):
        super().__init__(title, type_e, model, func, count, cost)

    def add_xerox_info(self, dpi, auto):
        self.info.update({"Разрешение": dpi})
        self.info.update({"Устройство подачи": auto})


pr = Printer('Склад 1', 'Принтер', 'HP', 'печать', 10, 1000)
pr.add_print_info(True, 'Лазерная')
print(pr)

dict_t = {}
dict_eq = {}

# отправка  оборудования на склад
while True:
    try:
        type_eq = input('Введите тип оборудования (окончание ввода - пустая строка): ')
        count_eq = input('Введите количество оборудования: ')
        if not type_eq:
            break
        else:
            if count_eq.isdigit():
                dict_t = {type_eq: count_eq}
                dict_eq.update(dict_t)
            else:
                raise DigitlError("Введено не число")
    except DigitlError as my_err:
        print(my_err)
    if not type_eq:
        break

to_wr = Printer.get_eq(dict_eq)
print(to_wr)

print(pr.send_eq('принтер', 2))