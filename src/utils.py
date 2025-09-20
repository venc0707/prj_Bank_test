import json
from os.path import dirname, join
import logging


logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("/home/user/PycharmProjects/Prj_Bank/logs/utils.log")
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def financial_transaction(filename: str) -> list[dict]:
    """возвращает список словарей с данными о финансовых транзакциях"""

    dir = dirname(dirname(__file__))
    path_filename = join(dir, f"data/{filename}")

    try:
        logger.info('Открывваем файл для чтения')
        with open(path_filename, "r", encoding="utf-8") as file:
            try:
                logger.info('Преобразовываем в python обьект')
                data = json.load(file)
            except json.JSONDecodeError as e:
                print(f"Ошибка декодирования JSON строки: {e}")
                logger.error(f'Ошибка: {e}')
                return []

            logger.info('Проверяем данные файла являются списком')
            if isinstance(data, list):
                logging.info('Возвращаем данные')
                return data
            else:
                print(f"Файл не список")
                logger.error('Файл не в формате списка')
                return []

    except FileNotFoundError:
        print(f"Файл не найден")
        logger.error('Файл не найден')
        return []


if __name__ == "__main__":
    print(financial_transaction("operations.json"))
