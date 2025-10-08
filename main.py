from src.counting_categories import process_bank_operations
from src.external_api import amount_transaction
from src.utils import financial_transaction
from src.get_data_is_csv_xlsx import get_data_is_csv_xlsx
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency
from src.process_bank_search import process_bank_search
from src.widget import get_date, mask_account_card


def main():
    """ Основной функциона проекта """

    print("""Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями. 
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
    """)

    try:
        while True:
            user_file_format = int(input())
            if user_file_format == 1:
                print('Для обработки выбран JSON-файл.')
                user_file_format = 'data/operations.json'
                open_file = financial_transaction(user_file_format)
                break
            elif user_file_format == 2:
                print('Для обработки выбран CSV-файл.')
                user_file_format = 'data/transactions.csv'
                open_file = get_data_is_csv_xlsx(user_file_format)
                break
            elif user_file_format == 3:
                print('Для обработки выбран XLSX-файл.')
                user_file_format = 'data/transactions_excel.xlsx'
                open_file = get_data_is_csv_xlsx(user_file_format)
                break
            else:
                print(f'Входные данные: {user_file_format}, данного пункта не в системе выбора,'
                      f' повторите попытку')

        print('''Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING''')
        while True:
            user_status_operations = str(input().upper())
            if user_status_operations == 'EXECUTED':
                print('Операции отфильтрованы по статусу "EXECUTED"')
                break
            elif user_status_operations == 'CANCELED':
                print('Операции отфильтрованы по статусу "CANCELED"')
                break
            elif user_status_operations == 'PENDING':
                print('Операции отфильтрованы по статусу "PENDING"')
                break
            else:
                print(f'Статус операции {user_status_operations} недоступен.\n'
                      f'Введите статус, по которому необходимо выполнить фильтрацию.\n'
                      f'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')

        try:
            user_sorted_deta = input('Отсортировать операции по дате? Да/Нет ').lower()
        except:
            raise f'Ошибка ввода сортировки операции, ожидается Да/Нет.'

        user_sorted_deta_flag = True
        if user_sorted_deta == 'да':
            user_sorted_deta_flag = input('Отсортировать по возрастанию или по убыванию? по возрастанию/по убыванию ')
            if user_sorted_deta_flag == 'по возрастанию':
                user_sorted_deta_flag = False
        try:
            user_currency = input('Выводить только рублевые транзакции? Да/Нет ').lower()
        except:
            raise f'Ошибка выбора валюты'

        user_words_description = None
        try:
            user_sorted_transactions_description = input(
                'Отфильтровать список транзакций по определенному слову в описании? Да/Нет ').lower()
            if user_sorted_transactions_description == 'да':
                user_words_description = input('Введите слова фильтрации  ')
        except:
            raise f'Ошибка фильтрации по описанию транзакции'

        print('Распечатываю итоговый список транзакций...')

        state_open_file = filter_by_state(open_file,
                                          user_status_operations)  # фильтрация по статусу: EXECUTED, CANCELED, PENDING

        date_state_open_file = sort_by_date(state_open_file, user_sorted_deta_flag)  # сортировка по дате

        if user_currency == 'да':  # вывод по валюте
            currency_date_state_open_file = [x for x in filter_by_currency(open_file, 'RUB')]
        else:
            currency_date_state_open_file = date_state_open_file

        if user_words_description:  # фильтрация по описанию
            description_currency_date_state_open_file = process_bank_search(currency_date_state_open_file,
                                                                            user_words_description)
        else:
            description_currency_date_state_open_file = currency_date_state_open_file

        # Вывод
        print(
            f'Всего банковских операций в выборке: {len(description_currency_date_state_open_file)}')

        if user_sorted_transactions_description == 'нет':
            counter = process_bank_operations(description_currency_date_state_open_file)
            for key, value in counter.items():
                print(f'{key}: {value}')

        for transaction in description_currency_date_state_open_file:
            print(f'\n{get_date(transaction['date'])} {transaction['description']}')
            if 'from' in transaction and isinstance(transaction.get('from'), str):
                print(f'{mask_account_card(transaction['from'])} -> {mask_account_card(transaction['to'])}')
            else:
                print(f'{mask_account_card(transaction['to'])}')

            if user_file_format.split('.')[-1] == 'csv' or user_file_format.split('.')[-1] == 'xlsx':
                if transaction.get('currency_code') != 'RUB':
                    print(f'Сумма: {transaction['amount']} {transaction['currency_code']}')
                else:
                    print(
                        f'Сумма: {amount_transaction(description_currency_date_state_open_file, transaction['id'])} руб.')
            else:
                if transaction.get('code') != 'RUB':
                    print(
                        f'Сумма: {transaction['operationAmount']['amount']} {transaction['operationAmount']['currency']['name']}')
                else:
                    print(
                        f'Сумма: {amount_transaction(description_currency_date_state_open_file, transaction['id'])} руб.')

    except Exception as ex:
        print(f'{ex}')


if __name__ == '__main__':
    main()
