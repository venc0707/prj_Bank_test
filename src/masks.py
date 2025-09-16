def get_mask_card_number(card_number: str) -> str:
    """Функцию маскировки номера банковской карты"""
    if not isinstance(card_number, str):
        raise TypeError("Не верный тип данных")
    if not len(card_number) == 16:
        raise ValueError("Неверный ввод")

    mask_card = f"{''.join(card_number[:4])} {''.join(card_number[4:6])}** **** {''.join(card_number[-4:])}"
    return mask_card


def get_mask_check(check_number: str) -> str:
    """Функцию маскировки номера банковского счета"""
    if not isinstance(check_number, str):
        raise TypeError("Не верный тип данных")
    if not len(check_number) == 20:
        raise ValueError("Неверный ввод")

    mask_check = f"**{''.join(check_number[-4:])}"
    return mask_check
