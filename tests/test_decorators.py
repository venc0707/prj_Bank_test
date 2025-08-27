import pytest

from src.decorators import log


def test_log(capsys):
    """тест на успешный вызов"""

    @log()
    def text(a):
        if a > 0:
            return 10 / a
        raise ValueError("отрицательное")

    text(5)
    captured = capsys.readouterr()
    assert captured.out == "text: completed\n"


def test_log_my_log_txt():
    """проверяем записи в логах"""
    my_log = "/home/user/PycharmProjects/Prj_Bank/src/my_log.txt"
    with open(my_log, "r", encoding="utf-8") as f:
        content = f.read()
        assert "text: completed" in content


def test_log_zero():
    """тест на ошибку"""

    @log()
    def text(a):
        if a > 0:
            return 10 / a
        raise ValueError("отрицательное")

    with pytest.raises(ValueError, match="отрицательное"):
        text(0)
