import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card() -> None:
    """Тест стандартного ввода"""
    assert mask_account_card("Maestro 1000200030004000") == "Maestro 1000 20** **** 4000"


def test_mask_account_card_check() -> None:
    """тест стандартного ввода"""
    assert mask_account_card("Счёт 10002000300040005000") == "Счёт **5000"


@pytest.mark.parametrize(
    "type_number, expected_result",
    [("Maestro 100020003000", ValueError), ("Счёт 100020003000", ValueError), ("", ValueError), (12345, TypeError)],
)
def test_mask_account_card_raise(type_number: str, expected_result: type[BaseException]) -> None:
    """проверка на ошибки"""
    with pytest.raises(expected_result):
        mask_account_card(type_number)


def test_get_data() -> None:
    """проверка стандартного ввода"""
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


@pytest.mark.parametrize(
    "date, expected_date",
    [
        ("2024-03-1102:26:18.671407", ValueError),
        ("", ValueError),
        (2024 - 10 - 11, TypeError),
        ("T02:26:18.671407", ValueError),
    ],
)
def test_test_get_data_raise(date: str, expected_date: type[BaseException]) -> None:
    """проверка на ошибки"""
    with pytest.raises(expected_date):
        get_date(date)
