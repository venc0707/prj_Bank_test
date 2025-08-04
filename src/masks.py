def get_mask_card_number(card_number: str) -> str:
    """Функцию маскировки номера банковской карты"""
    mask_card = f"{''.join(card_number[:4])} {''.join(card_number[4:6])}** **** {''.join(card_number[-4:])}"
    return mask_card


def get_mask_account(account_number: str) -> str:
    """Функцию маскировки номера банковского счета"""
    mask_account = f"**{''.join(account_number[-4:])}"
    return mask_account
