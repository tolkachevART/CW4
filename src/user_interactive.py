from src.json_worker import WorkWithJson
from src.parser import HH


class UserInteractive(WorkWithJson):
    """
    Класс, обеспечивающий взаимодействие с пользователем
    """

    def __init__(self, user_name: str):
        super().__init__()
        self.user_name = user_name
        self.vacancies_list = []

    @staticmethod
    def get_vacancies_list(keyword: str):
        """
        Получение с сайта HH списка вакансий
        :param keyword:
        :return:
        """

        hh = HH(keyword)
        return hh.load_vacancies()

    def get_vacancies_list_from_file(self) -> list[dict]:
        """
        Получение из файла списка вакансий
        :return:
        """

        work_file = WorkWithJson()
        self.vacancies_list = []
        for vac in work_file.read_file():
            self.vacancies_list.append(vac)
        return self.vacancies_list

    def get_top_n_for_salary(self, n: int) -> list[dict]:
        """
        Получение заданного пользователем количества вакансий с сортировкой
        по уровню зарплат (с убыванием)
        :param n:
        :return:
        """

        vac_filter = []
        for vac in self.vacancies_list:
            vac_filter.append(vac)

        sort_by_salary = sorted(vac_filter, key=lambda x: x.salary, reverse=True)
        return sort_by_salary[:n]

    def get_vacancy_from_keywords(self) -> list[dict]:
        """
        Получение списка вакансий по заданному ключевому слову
        :return:
        """
        keywords = input("Введите ключевое слово:  ")
        print()
        res = []
        for vacancy in self.vacancies_list:
            if vacancy.name.find(keywords) != -1:
                res.append(vacancy)

        return res
