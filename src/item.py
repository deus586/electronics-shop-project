from csv import DictReader


class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = [args[0], args[1], args[2]] if args[:3] else 'Файл повреждён'

    def __str__(self):
        return self.message


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return self.__name

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        raise TypeError

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) < 10:
            self.__name = new_name
        else:
            self.__name = new_name[:10]

    @classmethod
    def instantiate_from_csv(cls, path):
        try:
            with open(path, 'r', newline='', encoding='Windows-1251') as csv_file:
                reader = DictReader(csv_file)
                for row in reader:
                    print(len(row))
                    if len(row) == 3:
                        name = row['name']
                        price = float(row['price'])
                        quantity = int(row['quantity'])
                        cls.all.append(cls(name, price, quantity))
                    else:
                        raise InstantiateCSVError
        except FileNotFoundError:
            raise FileNotFoundError('Файл не найден')
        else:
            return cls.all

    @staticmethod
    def string_to_number(number: str):
        return int(float(number))
