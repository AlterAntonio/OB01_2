class Store():
    def __init__(self, name='Магаз', address='Местный', items={}):
        self.name = name
        self.address = address
        self.items = items


    def add_item(self, item, price=0):
        if item not in self.items.keys():
            self.items[item] = price
            print(f'Магазин "{self.name}: товар "{item}" добавлен в ассортимент по цене {price}')
        else:
            print(f'Магазин "{self.name}": товар с наименованием "{item}" уже есть в ассортименте по цене '
                  f'{self.items[item]}')

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]
            print(f'Магазин "{self.name}": товар "{item}" удалён из ассортимента.')
        else: print(f'Магазин "{self.name}: так товара с названием "{item}" и не было в наличии.')















            )