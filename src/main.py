from hh_parsing import HeadHunterInfo
from vacancies import Vacancies
from saving_information import SavingVacancies

if __name__ == "__main__":

    hh_ru = HeadHunterInfo()
    save = SavingVacancies(hh_ru.splitting_vacancies())
    save.add_vacancies()

    vacancies_list = []

    def user_interaction():
        """
        Функция для взаимодействия с пользователем.
        Выводит отфильтрованную информацию о вакансиях
        """

        name = input("Введите название вакансии: ")  # Например: "На удалёнке"
        top = int(input("Введите количество вакансий для проверки: "))  # Например: 8
        requirement = input("Введите ключевые слова для фильтрации вакансий по требованиям: ")  # Например: "Способен работать в команде"
        salary = input("Введите диапазон зарплаты: ")  # Например: "30000-40000"

        vacancies = save.getting_data(name, top, salary, requirement)
        save.delete_info()

        for vacancy in vacancies:
            information = Vacancies(vacancy)
            vacancies_list.append(information)

            print(f'{information}\n')

    user_interaction()
