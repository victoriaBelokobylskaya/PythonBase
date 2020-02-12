# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
# на ваше усмотрение.  Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
# завершать скрипт.

from termcolor import colored
from time import sleep


class TrafficLight():
    def __init__(self):
        self._color = 'red'

    # метод класса
    def running(self):
        i = 0
        while i <= 3:
            i += 1
            print(f'\nRound {i}')

            print(colored("Red", self._color))
            sleep(7)

            print(colored("Yellow", 'yellow'))
            sleep(2)

            print(colored("Green", 'green'))
            sleep(3)

        print('\nTrafficLigh finised')


trafic_lights = TrafficLight()
trafic_lights.running()
