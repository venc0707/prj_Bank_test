import json

from src.utils import financial_transaction


def test_finansical_transaction():
    with open("data/test.json", "w", encoding="utf-8") as f:
        data = [{"test": "test"}]
        json.dump(data, f)
    result = financial_transaction("test.json")
    assert result == [{"test": "test"}]


def test_finansical_transaction_FileNotFoundError():
    result = financial_transaction("test")
    assert result == []


def test_finansical_transaction_JSONDecodeError():
    with open("data/test.json2", "w", encoding="utf-8") as f:
        json.dump(('{"key": "value"'), f)
    result = financial_transaction("test.json2")
    assert result == []
