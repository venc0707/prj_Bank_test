import json
from os.path import dirname, join


def financial_transaction(filename: str) -> list[dict]:
    """возвращает список словарей с данными о финансовых транзакциях"""

    dir = dirname(dirname(__file__))
    path_filename = join(dir, f"data/{filename}")

    try:
        with open(path_filename, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError as e:
                print(f"Ошибка декодирования JSON строки: {e}")
                return []

            if isinstance(data, list):
                return data
            else:
                print(f"Файл не список")
                return []

    except FileNotFoundError:
        print(f"Файл не найден")
        return []


if __name__ == "__main__":
    print(financial_transaction("operations.json"))
