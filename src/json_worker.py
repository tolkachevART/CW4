import json
import os.path
from abc import ABC, abstractmethod


class FileWork(ABC):
    """
    Абстрактный класс, определяющий обязательный методы для классов-потомков
    """

    def __init__(self):
        pass

    @abstractmethod
    def read_file(self):
        """
        Чтение файла
        :return:
        """
        pass

    @abstractmethod
    def save_file(self, data):
        """
        Запись файла
        :return:
        """
        pass

    @abstractmethod
    def delete_file(self):
        """
        Удаление файла
        :return:
        """
        pass


class WorkWithJson(ABC):
    """
    Класс для работы с файлами
    """

    def __init__(self):
        self._file_name = ""
        self.abs_path = os.path.abspath("data/vacancies.json")

    def read_file(self) -> list[dict]:
        """
        Чтение файла JSON.
        :return: данные из файла в формате JSON.
        """
        with open(self.abs_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def save_file(self, data: list[dict]) -> None:
        """
        Запись данных в файл JSON.
        :param data: список словарей с данными для сохранения.
        :return: None
        """
        current_data = self.read_file()
        combined_data = current_data + data

        with open(self.abs_path, "w", encoding="utf-8") as file:
            json.dump(combined_data, file, ensure_ascii=False, indent=4)

    def delete_file(self) -> None:
        """
        Удаление файла JSON.
        :return: None
        """
        return os.remove(self.abs_path)
