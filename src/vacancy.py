class Vacancy:
    """
    Класс для работы с вакансиями
    """

    def __init__(self, name: str, area: str, salary: int):
        self.name = self.__validation_data(name)
        self.area = self.__validation_data(area)
        self.salary = salary

    def __str__(self):
        return (f"{self.name}\n"
                f"Город: {self.area}\n"
                f"Зарплата: {self.salary if self.salary else "Не указана"} \n")

    def __lt__(self, other):
        """
        Метод для сравнения вакансий по зарплате
        :param other:
        :return:
        """
        if not self.salary:
            return 0  # "Не указана"
        elif not other.salary:
            return 0  # "hi"
        elif self.salary < other.salary:
            return True
        else:
            return False

    @staticmethod
    def __validation_data(data):
        """
        Метод валидации данных: если данные отстутствуют, возвращается текст "Отсутствует"
        :param data:
        :return:
        """
        if data:
            return data
        else:
            return "Отсутствует"