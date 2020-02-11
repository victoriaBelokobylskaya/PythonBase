# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов
# сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив
# сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class Complex():
    def __init__(self, real, img):
        self.complex = complex(real, img)

    def __str__(self):
        return str(self.complex)

    def __add__(self, other):
        return self.complex + other.complex

    def __mul__(self, other):
        return self.complex * other.complex


my_compl = Complex(4,-2)
my_compl2 = Complex(2,-3)


print(f'{my_compl} + {my_compl2} = {my_compl + my_compl2}')
print(f'{my_compl} * {my_compl2} = {my_compl * my_compl2}')