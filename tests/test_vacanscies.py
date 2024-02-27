def test_init_vacancies(vacancies):
    assert vacancies.name == 'Удаленный диспетчер чатов (в Яндекс)'
    assert vacancies.url == 'https://api.hh.ru/areas/113'
    assert vacancies.salary_to == 44000


def test_salary(vacancies):
    assert vacancies.salary == '30000-44000'


def test_str(vacancies):
    assert vacancies.__str__() == ('Удаленный диспетчер чатов (в Яндекс)\n'
                                   'https://api.hh.ru/areas/113\n'
                                   '30000-44000\n'
                                   'Способен работать в команде. Способен принимать решения самостоятельно. '
                                   'Готов учиться и узнавать новое. Опыт работы в колл-центре или службе...')



