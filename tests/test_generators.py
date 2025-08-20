import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(transactions):
    generator = filter_by_currency(transactions, 'rub')
    assert next(generator) == {'id': 873106923, 'state': 'EXECUTED', 'date': '2019-03-23T01:09:46.296404', 'operationAmount': {'amount': '43318.34', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 44812258784861134719', 'to': 'Счет 74489636417521191160'}
    assert next(generator) == {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689', 'operationAmount': {'amount': '67314.70', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Visa Platinum 1246377376343588', 'to': 'Счет 14211924144426031657'}


def test_filter_by_currency_list():
    """Тестирование случая, когда нет подходящих транзакций"""
    generator = list(filter_by_currency([], 'eur'))
    assert generator == []


def test_filter_by_currency_not_znach():
    """Тестирование случая, когда нет подходящих транзакций"""
    transactions = [
        {
            "operationAmount": {
                "currency": {
                    "code": "EUR"
                }
            }
        }
    ]
    generator = list(filter_by_currency(transactions, 'usd'))
    assert generator == []


def test_transaction_descriptions(transactions):
    generator = transaction_descriptions(transactions)
    assert next(generator) == 'Перевод организации'
    assert next(generator) == 'Перевод со счета на счет'


def test_transaction_descriptions_not():
    generator = list(transaction_descriptions([]))
    assert generator == []


def test_transaction_descriptions_none():
    transactions = [
        {
            "description": "",
            "operationAmount": {
                "currency": {
                    "code": "EUR"
                }
            }
        }
    ]
    generator = transaction_descriptions(transactions)
    assert list(generator) == ['']


def test_card_number_generator():
    generator = card_number_generator(10000, 10003)
    assert next(generator) == '0000 0000 0001 0000'
    assert next(generator) == '0000 0000 0001 0001'
    assert next(generator) == '0000 0000 0001 0002'
    assert next(generator) == '0000 0000 0001 0003'


def test_card_number_generator_error1():
    generator = card_number_generator(0, 2)
    with pytest.raises(ValueError):
        next(generator)


def test_card_number_generator_error2():
    generator = card_number_generator(9999999999999998, 10000000000000000)
    with pytest.raises(ValueError):
        next(generator)





