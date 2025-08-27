import pytest
from src.decorators import log



def test_log(capsys):
    @log()
    def text(a):
        if a > 0:
            return 10 / a
        raise ValueError('отрицательное')

    text(5)
    captured = capsys.readouterr()
    assert captured.out == 'text: completed\n'


def test_log_zero():
    @log()
    def text(a):
        if a > 0:
            return 10 / a
        raise ValueError('отрицательное')
    
    with pytest.raises(ValueError, match='отрицательное'):
        text(0)




    

    

