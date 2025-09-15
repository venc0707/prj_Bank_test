import os

from src.utils import financial_transaction
import requests
from dotenv import load_dotenv


def amount_transaction(id_transaction: int) -> float:
    transactions = financial_transaction('operations.json')

    load_dotenv()
    headers = {
        'apikey': os.getenv('API_KEY')
    }

    for transaction in transactions:
        if transaction.get('id') == id_transaction:
            if transaction['operationAmount']['currency'].get('code') == 'RUB':
                return transaction['operationAmount']['amount']

            currency_code = transaction['operationAmount']['currency'].get('code')
            amount = transaction['operationAmount']['amount']

            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}"
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                result = response.json()['result']
                return result
            else:
                print(f'status code: {response.status_code}')


if __name__ == '__main__':
    print(amount_transaction(441945886))
    print(amount_transaction(41428829))
