from src.masks import get_mask_card_number, get_mask_check
import pytest


def test_get_mask_card_number():
    assert get_mask_card_number('1111222233334444') == '1111 22** **** 4444'


@pytest.mark.parametrize('card_number, expected_result', [('10002000300040005000', ValueError),
                                                          ('100020003000', ValueError),
                                                          (1000200030004000, TypeError),
                                                          ('', ValueError)
                                                          ])
def test_get_mask_card_number_raise(card_number, expected_result):
    with pytest.raises(expected_result) as exc_info:
        get_mask_card_number(card_number)


def test_get_mask_check():
    assert get_mask_check('10002000300040005000') == '**5000'


@pytest.mark.parametrize('check_number, expected_result', [('', ValueError),
                                                           (10002000300040005000, TypeError),
                                                           ('12345', ValueError),
                                                           ('100020003000400050006000', ValueError)
                                                           ])
def test_get_mask_check_number_raise(check_number, expected_result):
    with pytest.raises(expected_result) as exc_info:
        get_mask_check(check_number)
