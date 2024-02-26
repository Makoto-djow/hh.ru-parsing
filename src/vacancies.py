class Vacancies:
    """
    Класс для работы с вакансиями. Имеет функции сложения и сравнения вакансий
    """

    def __init__(self, info):
        """
        Инициализация атрибутов вакансий
        :param info: информация о вакансии
        """

        try:
            self.info = info
            self.name = self.info['name']
            self.url = self.info['area']['url']
            self.salary_from = self.info['salary']['from']
            self.salary_to = self.info['salary']['to']
            self.requirements = self.info['snippet']['requirement']
        except (KeyError, IndexError):
            print('Нет ключей или слишком большое число вывода вакансий')

    @property
    def salary(self):
        """
        Метод для объединения минимальной и максимальной зарплаты
        :return: возвращает строку с диапазоном зарплаты
        """

        return f"{self.salary_from}-{self.salary_to}"

    def __str__(self):
        """
        Информация для пользователя о вакансии
        :return: возвращает строку с информацией о вакансии(наимеенование, ссылка, зарплата, требования)
        """

        return f'{self.name}\n{self.url}\n{self.salary}\n{self.requirements}'

    def __lt__(self, other):
        return self.salary_from < other.salary_from or self.salary_to < other.salary_to

    def __le__(self, other):
        return self.salary_from <= other.salary_from or self.salary_to <= other.salary_to

    def __gt__(self, other):
        return self.salary_from > other.salary_from or self.salary_to > other.salary_to

    def __ge__(self, other):
        return self.salary_from >= other.salary_from or self.salary_to >= other.salary_to
