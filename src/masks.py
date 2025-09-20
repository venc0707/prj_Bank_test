import logging


logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("/home/user/PycharmProjects/Prj_Bank/logs/masks.log")
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функцию маскировки номера банковской карты"""
    logger.info('Проверяем входные данные')
    if not isinstance(card_number, str):
        raise TypeError("Не верный тип данных")
    if not len(card_number) == 16:
        raise ValueError("Неверный ввод")


    mask_card = f"{''.join(card_number[:4])} {''.join(card_number[4:6])}** **** {''.join(card_number[-4:])}"
    logger.info('возвращаем результат')
    return mask_card


def get_mask_check(check_number: str) -> str:
    """Функцию маскировки номера банковского счета"""
    logger.info('Проверяем входные данные')
    if not isinstance(check_number, str):
        raise TypeError("Не верный тип данных")
    if not len(check_number) == 20:
        raise ValueError("Неверный ввод")


    mask_check = f"**{''.join(check_number[-4:])}"
    logger.info('Возвращаем результат')
    return mask_check


if __name__ == "__main__":
    print(get_mask_card_number("1111222233334444"))