from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, supported_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.__number_of_sim = supported_sim

    def __repr__(self):
        return super().__repr__()[:-1] + f', {self.number_of_sim})'

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_num):
        if new_num > 0:
            self.__number_of_sim = new_num
        else:
            raise ValueError
