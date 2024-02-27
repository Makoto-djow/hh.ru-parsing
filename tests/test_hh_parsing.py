def test_hh_parsing(parsing):
    assert parsing.get_info()['items'][0]['name'] == "Удаленный диспетчер чатов (в Яндекс)"
    assert parsing.splitting_vacancies()[0]['area']['url'] == 'https://api.hh.ru/areas/113'
