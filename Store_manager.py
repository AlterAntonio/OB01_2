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

    def update_price(self, item, price):
        if item in self.items:
            if self.items[item] > price:
                print('(Тревога, зафиксировано снижение цены!)')
                before = self.items[item]
                discount = (before - price) / before * 100
                print(f'Магазин "{self.name}": (Тревога, зафиксировано снижение цены!)\nГрандиозные скидки!!! Горячее '
                      f'предложение!!!\n{item} по скидке в {discount}%!!!'
                      f'\nТеперь всего-лишь за {price}!!!')
            elif self.items[item] == price:
                print(f'Магазин "{self.name}": цена на "{item}" осталась прежней - {self.items[item]}')
            else: print(f'Магазин "{self.name}": новая цена на "{item}" - {price}')
        else: print(f'Магазин "{self.name}": товар с наименованием "{item}" отсутствует в ассортименте.')






