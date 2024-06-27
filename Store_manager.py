class Store:
    def __init__(self, name='Магаз', address='Местный', items={}):
        self.name = name
        self.address = address
        self.items = items

    def get_price(self, item):
        if item in self.items:
            print(f'Магазин "{self.name}: цена за одну единицу "{item}" - {self.items[item]}')
        else:
            print(f'Магазин "{self.name}: товара "{item}" нет в ассортименте')








