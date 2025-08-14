import re

from src.masks import get_mask_card_number, get_mask_check


def mask_account_card(type_number: str) -> str:
    """Функция возвращает: тип карты и номер(счет) карты"""
    if not isinstance(type_number, str):
        raise TypeError("Неверный тип даных")

    split_type_number = type_number.split()
    type_card = []
    ac_number = ""
    mask_card = ""
    for item in split_type_number:
        if re.fullmatch(r"^[a-zA-Z]+$", item):
            type_card.append(item)
            type_card_join = " ".join(type_card)
        elif re.fullmatch(r"^[а-яёА-ЯЁ]+$", item):
            type_card.append(item)
            type_card_join = " ".join(type_card)
        if item.isdigit():
            ac_number += item
    if len(ac_number) == 20:
        mask_card = get_mask_check(ac_number)
    elif len(ac_number) == 16:
        mask_card = get_mask_card_number(ac_number)
    else:
        raise ValueError("Неверный ввод")

    return str(f"{type_card_join} {mask_card}")


def get_date(date: str) -> str:
    """Функция возвращает дату в формате 'ДД.ММ.ГГГГ'"""
    if not isinstance(date, str):
        raise TypeError
    if "T" not in date:
        raise ValueError

    date_split = date.split("T")
    if date_split[0] == "":
        raise ValueError("Неверный ввод")
    year_mounth_day = date_split[0].split("-")

    return f"{year_mounth_day[-1]}.{year_mounth_day[1]}.{year_mounth_day[0]}"


if __name__ == "__main__":
    #  type_number = 'Maestro 1596837868705199'
    # type_number = 'Visa Platinum 8990922113665229'
    type_number = "Счет 35383033474447895560"
    print(mask_account_card(type_number))  # Visa Platinum 7000 79** **** 6361 | Счет **4305

    date = "2024-03-11T02:26:18.671407"
    print(get_date(date))  # "11.03.2024"
