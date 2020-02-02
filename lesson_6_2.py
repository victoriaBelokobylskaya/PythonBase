class Road():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def square(self):
        vol = 25
        width_sm = 5
        itog = self.length * self.width * vol * width_sm / 1000
        return itog


road_1 = Road(20, 5000)
print(f'Нужно {road_1.square()} тонн асфальта')
