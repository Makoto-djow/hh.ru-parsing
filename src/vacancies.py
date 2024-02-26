from hh_parsing import HeadHunterInfo


class Vacancies:

    def __init__(self, info):

        self.info = info
        self.name = self.info['items'][0]['name']
        self.url = self.info['items'][0]['area']['url']
        self.salary = self.info['items'][0]['salary']['to']
        # self.description = self.info['items'][0]
        self.requirements = self.info['items'][0]['snippet']['requirement']

    def __lt__(self, other):
        try:
            return self.salary < other.salary
        except ValueError:
            print('Неправильные данные')

    def __le__(self, other):
        try:
            return self <= other
        except ValueError:
            print('Неправильные данные')

    def __gt__(self, other):
        try:
            return self > other
        except ValueError:
            print('Неправильные данные')

    def __ge__(self, other):
        try:
            return self >= other
        except ValueError:
            print('Неправильные данные')

    def validation(self):
        pass
