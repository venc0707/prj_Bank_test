import os

import requests
from dotenv import load_dotenv

try:
    from src.utils import financial_transaction
except ImportError:
    # Альтернативный вариант - добавляем путь к sys.path
    import os
    import sys

    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from src.utils import financial_transaction


def amount_transaction(transactions:list[dict], id_transaction: int) -> float:
    """возвращает сумму транзакции в рублях"""
    load_dotenv()

    #transactions = financial_transaction("operations.json")

    for transaction in transactions:
        if transaction.get("id") == id_transaction:

            if "operationAmount" in transaction and isinstance(transaction["operationAmount"], dict):
                currency_code = transaction["operationAmount"]["currency"].get("code")
                amount = transaction["operationAmount"].get("amount")
            else:
                currency_code = transaction.get("currency_code")
                amount = transaction.get("amount")

            if currency_code is None or amount is None:
                print(f"Неполные данные в транзакции {id_transaction}")
                return 0.0

            if currency_code == "RUB":
                return float(amount)

            headers = {"apikey": os.getenv("API_KEY")}
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}"

            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                result = response.json().get("result")
                if result is not None:
                    return round(float(result), 2)
                else:
                    print("Не удалось получить результат конвертации")
                    return 0.0
            else:
                print(f"status code: {response.status_code}")
                return 0.0

    print(f"Транзакция с ID {id_transaction} не найдена")
    return 0.0


if __name__ == "__main__":

    data = ''
    # print(amount_transaction(441945886))
    print(amount_transaction(data, 3235160))
