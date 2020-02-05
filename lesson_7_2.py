from abc import ABC, abstractmethod


class Сlothes(ABC):
    def __init__(self, title):
        self.title = title

    @abstractmethod
    def calc_clothes(self):
        print('Расчет ткани')


class Coat(Сlothes):
    def calc_clothes(self):
        print(f'Расчет ткани. Для пальто нужно: {self.title / 6.5 + 0.5:0.2f}')


class Costume(Сlothes):
    @property
    def calc_clothes(self):
        print(f'Расчет ткани. Для костюма нужно: {2 * self.title + 0.3:0.2f}')


my_coat = Coat(5)
my_costume = Costume(3)

my_coat.calc_clothes()
my_costume.calc_clothes
