from abc import ABC, abstractmethod

import requests


class Parser(ABC):
    """
    Абстрактный класс для парсинга вакансий.
    """

    @abstractmethod
    def load_vacancies(self):
        """
               Метод для загрузки вакансий.
               """
        pass


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self, keyword: str):
        """
              Конструктор класса HH.

              :param keyword: ключевое слово для поиска вакансий.
        """
        self._url = 'https://api.hh.ru/vacancies'
        self._headers = {'User-Agent': 'HH-User-Agent'}
        self._params = {'text': keyword, 'page': 0, 'per_page': 100}

    def load_vacancies(self) -> list[dict]:
        """
               Загрузка вакансий с использованием API HeadHunter.

               :return: список вакансий.
               """
        vacancies = []

        while self._params.get('page') != 1:
            response = requests.get(self._url, headers=self._headers, params=self._params)
            vacancies = response.json()['items']
            vacancies.extend(vacancies)
            self._params['page'] += 1

        return vacancies
