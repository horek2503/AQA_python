"""
Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру.
Властивості по типу “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор.
Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.
"""
from abc import ABC, abstractmethod

class Figure(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetry(self):
        pass

    @staticmethod
    def validate_sides(sides: list[int|float]):
        for side in sides:
            if not isinstance(side, (int, float)) or side <=0:
                raise ValueError("Side must be a positive number!")

class Square(Figure):
    def __init__(self, side: int|float):
        Figure.validate_sides([side])
        self.__side = side

    def area(self):
        return self.__side ** 2

    def perimetry(self):
        return 4 * self.__side

class Rectangle(Figure):
    def __init__(self, side_a: int | float, side_b: int | float):
        Figure.validate_sides([side_a, side_b])
        self.__side_a = side_a
        self.__side_b = side_b

    def area(self):
        return self.__side_a * self.__side_b

    def perimetry(self):
        return 2 * self.__side_a + 2 * self.__side_b

class Triangle(Figure):
    def __init__(self, side_a: int | float, side_b: int | float, side_c: int | float):
        Figure.validate_sides([side_a, side_b, side_c])
        # Specific side validation for triangle
        if ((side_a + side_b <= side_c)
                or (side_b + side_c <= side_a)
                or (side_a + side_c <= side_b)):
            raise ValueError("Sum of two triangle sides must be greater than third side!")
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c

    def area(self):
        p = (self.__side_a + self.__side_b + self.__side_c) / 2
        return (p * (p - self.__side_a) * (p - self.__side_b) * (p - self.__side_c)) ** 0.5

    def perimetry(self):
        return self.__side_a + self.__side_b + self.__side_c

figures_list = list()
figures_list.append(Square(side = 2))
figures_list.append(Rectangle(5, 8))
figures_list.append(Triangle(4 , 2, 5))

for figure in figures_list:
    print(f'Current figure is a {figure.__class__.__name__} with P = {figure.perimetry()}, S = {figure.area()}')