# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
# (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
# Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен
# выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
from termcolor import colored


class Stationery():
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
        self.font = 'bold'

    def draw(self):
        print(f'This is {self.font} pen')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
        self.hardness = 'HB'

    def draw(self):
        print(f'This is {self.hardness} pencil')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
        self.color = 'red'

    def draw(self):
        print(colored(f'This is {self.color} handle', self.color))


my_pen = Pen('My pen')
my_pen.draw()

my_pencil = Pencil('My pencil')
my_pencil.draw()

my_handle = Handle('My handle')
my_handle.draw()