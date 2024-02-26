def test_saving_information(save_get):
    assert save_get[0]['id'] == '93670505'
    assert save_get[0]['response_letter_required'] is False
