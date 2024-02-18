# TODO Написать 3 класса с документацией и аннотацией типов

class Vector:                                                  # класс вектор
    def __init__(self, a, b):
        self.a = a     #координата OX
        self.b = b     #координата OY

    def __str__(self) -> str:
        """ Записывание данных о координатах вектора

        :return: координаты вектора

        >>> v1 = Vector(1,6)
        >>> v2 = Vector(2, 9)

        """
        return 'Vector ({}, {})'.format(self.a, self.b)

    def __add__(self, other):
        """ Сложение векторов по значениям х и у
        """
        return Vector(self.a + other.a, self.b + other.b)


class Square:   #площадь прямоугольников
    def __init__(self, a, b):
        self.a = a  #длина
        self.b = b    #ширина

    def __str__(self) -> str:
        """ Введение значения длины и ширины прямоугольника
        >>> s1 = Square(2, 10)
        :return: Значение прямоугольника
        """
        return 'Square ({}, {})'.format(self.a, self.b)

    def __mul__(self, a, b):
        """ Высчитывание площади прямоугольника
        """

        return Square(self.a * self.b)

class Value:   #объём прарллелепипеда
    def __init__(self, a, b, c):
        self.a = a   #длина
        self.b = b   #ширина
        self.c = c   #высота

    def __int__(self) -> str:
        """ Введение значения длины, ширины и высоты прямоугольника
        >>> s1 = Value(2, 10, 6)
        :return: Значение параллелепипеда
        """
        return 'Value ({}, {}, {})'.format(self.a, self.b, self.c)

    def __mul__(self, a, b, c):
        """ Высчитывание объёма параллелипипеда
        """
        return Value(self.a * self.b * self.c)

if __name__ == "__main__":

    v1 = Vector(2, 5)
    v2 = Vector(3, 4)

    print(v1 + v2)

    print(Square(2 * 2))

    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
