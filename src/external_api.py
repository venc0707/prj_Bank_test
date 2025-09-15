import os

import requests
from dotenv import load_dotenv

try:
    from src.utils import financial_transaction
except ImportError:
    # Альтернативный вариант - добавляем путь к sys.path
    import sys
    import os
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from src.utils import financial_transaction


def amount_transaction(id_transaction: int) -> float:
    transactions = financial_transaction('operations.json')

    load_dotenv()

    for transaction in transactions:
        if transaction.get('id') == id_transaction:

            currency_code = transaction['operationAmount']['currency'].get('code')
            amount = transaction['operationAmount']['amount']

            if currency_code == 'RUB':
                return amount

            headers = {'apikey': os.getenv('API_KEY')}
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}"
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                result = response.json()['result']
                return result
            else:
                print(f'status code: {response.status_code}')


if __name__ == '__main__':
    amount_transaction(441945886)
    print(amount_transaction(41428829))
