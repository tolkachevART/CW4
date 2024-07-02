
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