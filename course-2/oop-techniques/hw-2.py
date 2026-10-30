class Newspaper:
    def __init__(self, __name, year: int, month: int, day_of_month: int, is_finnish: bool):
        self.__name = __name
        self.year = year
        self.month = month
        self.day_of_month = day_of_month
        self.is_finnish = is_finnish

    def __str__(self):
        return f"{self.__name} {self.day_of_month}.{self.month}.{self.year}"

    def get_name(self):
        return self.__name

news = Newspaper("Hesari", 2026, 10, 30, True)

print(news)
print(news.get_name())
