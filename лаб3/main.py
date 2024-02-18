class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def name(self):
        return self.name

    @property
    def author(self):
        return self.author


    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook:
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self.pages

    @pages.setter
    def pages(self, value):
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным")

        if not isinstance(value, int):
            raise ValueError("Страницы должны быть целыми")

        self._pages = value

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}. Страницы {self.pages}"


class AudioBook:
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if value <= 0:
            raise ValueError("Длительность должна быть положительной")

        if not isinstance(value, float):
            raise ValueError("Длительность должна быть цислом с плавающей запятой")

        self._duration = value

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}. Длительность {self.duration}"
