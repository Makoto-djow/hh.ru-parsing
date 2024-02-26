import requests
from src.hh_abstract_class import HHAbstract


class HeadHunterInfo(HHAbstract):
    """
    Получает данные по вакансиям через GET-запрос в функции get_info.
    Формирует список вакансий в функции splitting_vacancies
    """

    def __init__(self):
        """
        Инициализация ссылки на сайт
        """

        self.__url = 'https://api.hh.ru/vacancies'
        self.vacancies_info = None

    def get_info(self):
        """
        Получение информации
        :return: возвращает данные о вакансиях
        """

        super().get_info()
        response = requests.get(self.__url)
        self.vacancies_info = response.json()
        return self.vacancies_info

    def splitting_vacancies(self):
        """
        Оформление информации в список
        :return: возвращает список вакансий
        """

        if self.vacancies_info is None:
            self.get_info()
        list_vacancies = []
        for vacancy in self.vacancies_info['items']:
            list_vacancies.append(vacancy)
        return list_vacancies
