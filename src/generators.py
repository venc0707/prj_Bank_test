from typing import Generator, Dict, Any, Iterator


def filter_by_currency(transactions: list[Dict[str, Any]], currency_name: str) -> Iterator[Dict[str, Any]]:
    """возвращает итератор с транзакциями по названию валюты"""
    currency_name = currency_name.upper()
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_name:
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
