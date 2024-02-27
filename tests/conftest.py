import pytest

from src.hh_parsing import HeadHunterInfo
from src.saving_information import SavingVacancies
from src.vacancies import Vacancies


@pytest.fixture
def parsing():
    head_hunter = HeadHunterInfo()
    return head_hunter


@pytest.fixture
def attributes():
    name = 'Менеджер'
    top = 10
    requirement = 'Способен работать'
    salar = '40000-50000'
    data_list = [name, top, requirement, salar]
    return data_list


@pytest.fixture
def save(parsing):
    saving_info = SavingVacancies(parsing)
    return saving_info


@pytest.fixture
def save_get(save, attributes):
    get = save.getting_data(attributes[0], attributes[1], attributes[2], attributes[3])
    return get


@pytest.fixture
def vacancies(save_get):
    for get in save_get:
        vacancy = Vacancies(get)
        return vacancy
