from abc import ABC, abstractmethod


class HHAbstract(ABC):
    """
    Абстрактный класс для отправки запроса и получения данных
    """

    @abstractmethod
    def get_info(self):
        pass


class AddingVacancies(ABC):
    """
    Абстрактный класс для добавления вакансий в файл,
    получения вакансий по введённым критериям и удаления вакансий из файла
    """

    @abstractmethod
    def add_vacancies(self):
        pass

    @abstractmethod
    def getting_data(self, name, top, salary, requirement):
        pass

    @abstractmethod
    def delete_info(self):
        pass
