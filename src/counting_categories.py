from collections import Counter


def process_bank_operations(data: list[dict], categories: list = None ) -> dict: # , categories: list
    """ возвращает кол-во операций в каждой категории """
    try:
        data_list = [transaction['description'] for transaction in data]
        count_operations = Counter(data_list)
        return count_operations

    except Exception as e:
        print(f'{e}')


if __name__ == '__main__':
    data = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431"
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        }
    ]

    categories = ['Перевод организации', 'Открытие вклада']

    print(process_bank_operations(data, categories))

    data_1 = [f'{x}:{i}' for x, i in list(process_bank_operations(data, categories).items())]
    print(data_1)


