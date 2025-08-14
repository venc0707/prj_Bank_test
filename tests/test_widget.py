from src.widget import mask_account_card, get_date
import pytest


def test_mask_account_card():
    assert mask_account_card('Maestro 1000200030004000') == 'Maestro 1000 20** **** 4000'


def test_mask_account_card_check():
    assert mask_account_card('Счёт 10002000300040005000') == 'Счёт **5000'


@pytest.mark.parametrize('type_number, expected_result', [('Maestro 100020003000', ValueError),
                                                          ('Счёт 100020003000', ValueError),
                                                          ('', ValueError),
                                                          (12345, TypeError)
                                                          ])
def test_mask_account_card_raise(type_number, expected_result):
    with pytest.raises(expected_result) as exc_info:
        mask_account_card(type_number)


def test_get_data():
    assert get_date('2024-03-11T02:26:18.671407') == "11.03.2024"


@pytest.mark.parametrize('date, expected_date', [('2024-03-1102:26:18.671407', ValueError),
                                                 ('', ValueError),
                                                 (2024 - 10 - 11, TypeError),
                                                 ])
def test_test_get_data_raise(date, expected_date):
    with pytest.raises(expected_date) as exc_info:
        get_date(date)
