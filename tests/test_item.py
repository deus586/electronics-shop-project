"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def items():
    item1 = Item('Phone', 10000, 10)
    item2 = Item('Laptop', 40000, 3)
    return {'first test': item1, 'second test': item2}


def test_total_price(items):
    assert items['first test'].calculate_total_price() == 100000
    assert items['second test'].calculate_total_price() == 120000


def test_price(items):
    Item.pay_rate = 0.8
    items['first test'].apply_discount()
    assert items['first test'].price == 8000
    assert items['second test'].price == 40000
