from hh_parsing import HeadHunterInfo
from vacancies import Vacancies

if __name__ == "__main__":

    headhunter = HeadHunterInfo()
    vacancies = Vacancies(headhunter.get_info())

    # print(headhunter.get_info()['items'])
    print(headhunter.get_info()['items'])

