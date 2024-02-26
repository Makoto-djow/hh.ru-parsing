import json
import requests
from src.hh_abstract_class import HHAbstract


class HeadHunterInfo(HHAbstract):
    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'

    def get_info(self):
        super().get_info()
        response = requests.get(self.__url)
        vacancies_info = response.json()
        # return json.dumps(vacancies_info, indent=4, ensure_ascii=False)
        return vacancies_info

    def changed(self, info):
        info['items'].split()

p = HeadHunterInfo()  #
print(type(p.get_info()))  #
