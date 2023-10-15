"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
import os
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


def test_name(items):
    assert items['first test'].name == 'Phone'
    assert items['second test'].name == 'Laptop'


def test_instantiate():
    os.chdir('..')
    Item.instantiate_from_csv('src/items.csv')
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'
    assert item1.price == 100


def test_string_to_number():
    assert Item.string_to_number('0') == 0
    assert Item.string_to_number('1000') == 1000
