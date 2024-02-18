class Cars:
    def __init__(self, brand: str, color: str) -> None: # ввод двух атрибутов: марка и цвет
        self.brand = brand
        self.color = color

    @ property  # марку автомобиля нельзя поменять
    def brand(self):
        return self.brand

    def __str__(self) -> str: # данные автомобиля
        return f"{self.color} {self.brand}"

    def __repr__(self) -> str: # название класса и данные класса
        return f"{self.__class__.__name__}({self.brand}, {self.color})"

class Passengers_cars(Cars): # дочерний класс Автомобили - Легковой автомобиль
    def __init__(self, brand: str, color: str, body: str) -> None: # ввод данных из базового класса + добавление атрибута кузов
        super().__init__(brand, color)
        self.body = body

    @property # кузов автомобиля нельзя поменять
    def body(self):
        return self.body

    def move(self, speed: int) -> str: # пишет информацию об автомобиле и её скорость

        if speed < 0: # проверка значения скорости
            raise ValueError("Скорость должна быть положительной")

        if not isinstance(speed, int):
            raise ValueError("Значение скорости должна быть целой")

        return f"The {self.color}{self.body} {self.brand} едет со скоростью {speed} километров в час"

    def __str__(self) -> str: #данные легкового автомобиля
        return f"{self.color} {self.body} {self.brand}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.brand}, {self.color}, {self.body})"

class Trucks(Cars): #дочерний класс Автомобили - Грузовой автомобиль
    def __init__(self, brand: str, colour: str, capacity: int): #ввод данных из базового класса + добавление атрибута вместительность
        super().__init__(brand, colour)
        self.capacity = capacity

    @property # вместительность грузового автомобиля нельзя изменить
    def capacity(self):
        return self.capacity

    @capacity.setter # проверка значения вместительность
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Вместительность должна быть положительной")
        self.capacity = value


    def __str__(self) -> str:# данные грузовго автомобиля
        return f"{self.color}{self.brand}{self.capacity}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.brand}, {self.color}, {self.capacity})"

if __name__ == "__main__":
    # Write your solution here
    car1 = Cars('mazda', 'black') # вызов класса Автомобили
    print(car1)
    car2 = Passengers_cars('suzuki', 'white', 'sedan') # вызов класса Легковые автомобили
    v_car2 = Passengers_cars.move(15) # вызов метода движение
    v1_car2 = Passengers_cars.move(-15) # проверка метода на отрицательном цначении
    print(car2, v1_car2, v_car2)
    car3 = Trucks('gaz', 'grey', 1000) # вызов класса Грузовой автомобиль
    print(car3)
    car4 = Trucks('gaz', 'grey', -1000) # проверка значения вместительность на отрицательном значении
    print(car4)

