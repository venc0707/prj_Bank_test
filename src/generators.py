from typing import Generator, Dict, Any, Iterator


def filter_by_currency(transactions: list[Dict[str, Any]], currency_name: str) -> Iterator[Dict[str, Any]]:
    """возвращает итератор с транзакциями по названию валюты"""
    currency_name = currency_name.upper()
    for transaction in transactions:
        if "operationAmount" in transaction:
            if transaction["operationAmount"]["currency"]["code"] == currency_name:
                yield transaction
        else:
            if transaction["currency_code"] == currency_name:
               yield transaction


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """возвращает описание каждой операции"""
    descriptions = (transaction["description"] for transaction in transactions)
    for description in descriptions:
        yield description


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """выдает номера банковских карт в формате
    XXXX XXXX XXXX XXXX"""
    numbers = range(start, end + 1)
    mask_card = "0000000000000000"
    if start >= 1 and end <= 9999999999999999:
        for num in numbers:
            new_card = mask_card[: len(mask_card) - len(str(num))]
            new_card += str(num)

            yield (f"{new_card[:4]} {new_card[4:8]} {new_card[8:12]} {new_card[12:16]}")
    else:
        raise ValueError("неверный диапазон")


if __name__ == '__main__':
    data =  [{'id': 4699552.0, 'state': 'EXECUTED', 'date': '2022-03-23T08:29:37Z', 'amount': 23423.0, 'currency_name': 'Peso', 'currency_code': 'PHP', 'from': 'Discover 7269000803370165', 'to': 'American Express 1963030970727681', 'description': 'Перевод с карты на карту'}]

    print(next(filter_by_currency(data, 'PHP')))
    currency_date_state_open_file = [x for x in filter_by_currency(data, 'RUB')]
    currency_date_state_open_file1 = [x for x in filter_by_currency(data, 'php')]
    print(currency_date_state_open_file)
    print(currency_date_state_open_file1)