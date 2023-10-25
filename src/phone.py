from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, supported_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.number_of_sim = supported_sim

    def __repr__(self):
        return super().__repr__()[:-1] + f', {self.number_of_sim})'
