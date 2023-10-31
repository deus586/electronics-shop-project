"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
import os
from src.item import Item, InstantiateCSVError
from src.phone import Phone


@pytest.fixture
def items():
    item1 = Item('Phone', 10000, 10)
    item2 = Item('Laptop', 40000, 3)
    phone1 = Phone('Phone', 100000, 10, 3)
    return {'first test': item1, 'second test': item2, 'phone test': phone1}


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


def test_str(items):
    assert str(items['first test']) == 'Phone'
    assert str(items['second test']) == 'Laptop'


def test_repr(items):
    assert repr(items['first test']) == "Item('Phone', 10000, 10)"
    assert repr(items['second test']) == "Item('Laptop', 40000, 3)"


def test_instantiate():
    os.chdir('..')
    Item.instantiate_from_csv('src/items.csv')
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'
    assert item1.price == 100


def test_string_to_number():
    assert Item.string_to_number('0') == 0
    assert Item.string_to_number('1000') == 1000


def test_phone(items):

    phone1 = items['phone test']
    assert phone1.name == 'Phone'
    assert phone1.number_of_sim == 3


def test_add(items):
    item = items['first test']
    phone = items['phone test']

    assert item + phone == 20
    assert phone + item == 20
    try:
        assert item + 10 == 20
        assert phone + 10 == 20
    except:
        print('TypeError')


def test_exc():
    with pytest.raises(FileNotFoundError, match='Файл не найден'):
        Item.instantiate_from_csv('some_csv.csv')
        # Проверка корректноссти регистра
        Item.instantiate_from_csv('ITEMS.csv')
    with pytest.raises(InstantiateCSVError, match='Файл повреждён'):
        Item.instantiate_from_csv('src/without_last_column.csv')
