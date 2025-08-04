def get_mask_card_number(card_number: str) -> str:
    """Функцию маскировки номера банковской карты"""
    mask_card = f"{''.join(card_number[:4])} {''.join(card_number[4:6])}** **** {''.join(card_number[-4:])}"
    return mask_card


def get_mask_check(check_number: str) -> str:
    """Функцию маскировки номера банковского счета"""
    mask_check = f"**{''.join(check_number[-4:])}"
    return mask_check
