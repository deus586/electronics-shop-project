from src.item import Item
import os

if __name__ == '__main__':
    os.chdir('..')
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv('src/item.csv')
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    Item.instantiate_from_csv('src/without_last_column.csv')
    # InstantiateCSVError: Файл item.csv поврежден
