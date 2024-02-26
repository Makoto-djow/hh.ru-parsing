import json

from hh_abstract_class import AddingVacancies


class SavingVacancies(AddingVacancies):
    """
    Класс для сохранения информации в файл,
    получение вакансий по введённым критериям и удаление ненужных вакансий из файла
    """

    def __init__(self, data):
        """
        Инициализация данных, файла и списка с вакансиями
        :param data: данные о вакансиях
        """

        self.__file = None
        self.__data = data
        self.__list_vacancy = []

    def add_vacancies(self):
        """
        Добавляет список вакансий в JSON-файл
        """

        super().add_vacancies()
        try:
            with open('../data/vacancies_data.json', 'w', encoding='utf-8') as file:
                file.write(json.dumps(self.__data, indent=4, ensure_ascii=False))
        except FileNotFoundError:
            print('Файл не существует')

    def getting_data(self, name, top, salary, requirement):
        """
        Получает вакансии по введённым критериям
        :param name: Название вакансии
        :param top: Количество вакансий
        :param salary: Зарплата
        :param requirement: Требования
        :return: Возвращает список найденных вакансий из файла по введённым критериям
        """

        super().getting_data(name, top, salary, requirement)

        salary_list = salary.split('-')
        salary_from, salary_to = salary_list[0], salary_list[1]
        with open('../data/vacancies_data.json', 'r+', encoding='utf-8') as file:
            for vacancy in json.load(file)[:top]:
                if name in vacancy['name']:
                    self.__list_vacancy.append(vacancy)

                if not vacancy['salary'] is None:
                    if vacancy['salary']['from'] == salary_from and vacancy['salary']['to'] == salary_to:
                        self.__list_vacancy.append(vacancy)

                if requirement in vacancy['snippet']['requirement']:
                    self.__list_vacancy.append(vacancy)
        return self.__list_vacancy

    def delete_info(self):
        """
        Удаляет все вакансии из файла не попадающие под критерии
        :return: Обновлённый JSON-файл
        """

        super().delete_info()
        with open('../data/vacancies_data.json', 'r', encoding='utf-8') as file:
            json_file = json.load(file)
            keys_to_delete = []
            for vacancy in json_file:
                if vacancy not in self.__list_vacancy:
                    keys_to_delete.append(vacancy)

            for key in keys_to_delete:
                delete_index = json_file.index(key)
                del json_file[delete_index]
        with open('../data/vacancies_data.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps(json_file, indent=4, ensure_ascii=False))
