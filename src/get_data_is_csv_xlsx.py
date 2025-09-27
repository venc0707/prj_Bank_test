import pandas as pd


def get_data_is_csv_xlsx(path_file: str) -> list[dict]:
    """возвращает список словарей с данными о финансовых транзакциях"""
    try:
        if not path_file:
            raise f'Fail not Found {path_file}'
        file = path_file.split('.')
        if file[-1] == 'csv':
            df = pd.read_csv(path_file, delimiter=';')
            return df.to_dict('records')
        if file[-1] == 'xlsx':
            df = pd.read_excel(path_file, engine='openpyxl')
            return df.to_dict('records')

    except ImportError as e:
        print(f'Ошибка: {e}')


if __name__ == '__main__':
    print(get_data_is_csv_xlsx('../data/transactions.csv'))
    print(get_data_is_csv_xlsx('../data/transactions_excel.xlsx'))
