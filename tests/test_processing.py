import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def new_list() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state(new_list: list[dict]) -> None:
    """тест стандартный ввод"""
    assert filter_by_state(new_list) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
    ]


@pytest.mark.parametrize("state, expected_list", [("date", []), ("", []), (123, [])])
def test_filter_by_state_param(new_list: list[dict], state: str, expected_list: dict) -> None:
    """проверка на state некоректных данных"""
    assert filter_by_state(new_list, state) == expected_list


def test_sort_by_date(new_list: list[dict]) -> None:
    """тест фильтрация по убыванию"""
    assert sort_by_date(new_list) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_false(new_list: list[dict]) -> None:
    """тест на фильтрацию  по возрастанию"""
    assert sort_by_date(new_list, False) == [
        {"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def list_date() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-0318:35:29.512364"},
        {"id": 939719570, "state": "CANCELED", "date": "aaaaaaaaaaaaaaaaaaaaa"},
        {"id": 594226727, "state": "EXECUTED", "date": "111111111111111"},
        {"id": 615064591, "state": "CANCELED", "date": 2024},
    ]


def test_sort_by_incorrect_date(list_date: list[dict]) -> None:
    """проверка на ошибки"""
    with pytest.raises(ValueError):
        sort_by_date(list_date)
