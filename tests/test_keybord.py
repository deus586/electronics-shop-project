import pytest
from src.keyboard import Keyboard


@pytest.fixture
def items():
    kb1 = Keyboard('keyboard1', 10000, 10)
    kb2 = Keyboard('keyboard2', 40000, 3)
    return {'first test': kb1, 'second test': kb2}


def test_visual(items):
    assert repr(items['first test']) == "Keyboard('keyboard1', 10000, 10)"
    assert str(items['second test']) == 'keyboard2'
    assert str(items['first test'].language) == 'EN'


def test_change_lang(items):
    items['first test'].change_lang()
    assert str(items['first test'].language) == 'RU'
