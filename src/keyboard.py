from src.item import Item


class MixinLang:
    CHG_LANG = {'EN': 'RU', 'RU': 'EN'}

    def __init__(self):
        self.__language = 'EN'
        self.chg_lang = self.CHG_LANG

    def change_lang(self):
        self.__language = self.chg_lang.get(self.language)

    @property
    def language(self):
        return self.__language

    def __str__(self):
        return f'{self.__language}'


class Keyboard(Item, MixinLang):
    pass


