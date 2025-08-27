from src.decorators import log


def test_log_capsys(capsys):
    @log
    def hi():
        return 'hi'
    captured = capsys.readouterr()
    assert captured.out == hi

