class Store:
    def __init__(self, name='Магаз', address='Местный', items={}):
        self.name = name
        self.address = address
        self.items = items

    def add_item(self, item, price=0):
        if item not in self.items.keys():
            self.items[item] = price
            print(f'Магазин "{self.name}": товар "{item}" добавлен в ассортимент по цене {price}')
        else:
            print(f'Магазин "{self.name}": товар с наименованием "{item}" уже есть в ассортименте по цене '
                  f'{self.items[item]}')

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]
            print(f'Магазин "{self.name}": товар "{item}" удалён из ассортимента.')
        else:
            print(f'Магазин "{self.name}": так товара с названием "{item}" и не было в наличии.')

    def items_list(self):
        print(f'Магазин "{self.name}", вот что мы предлагаем нашим преданным клиентам:')
        if self.items is None:
            print('Упс, пока что ничего:(')
        else:
            for item, price in self.items.items():
                print(f'{item} - {price}')

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
            else:
                print(f'Магазин "{self.name}": новая цена на "{item}" - {price}')
        else:
            print(f'Магазин "{self.name}": товар с наименованием "{item}" отсутствует в ассортименте.')


test_list = {'Молоко': 60, 'Сыр': 300, 'Яблоки': 90, 'Бананы': 50, 'Шоколад': 100, 'Кофе': 400, 'Чай': 150,
             'Мясо': 350, 'Рыба': 400}
magic_list = {'Волшебная палочка': 1200, 'Кристалл предсказаний': 3000, 'Набор алхимика': 2500,
              'Мантия невидимости': 4500, 'Зелье мудрости': 800}
space_list = {'Гипердвигатель': 150000, 'Квантовый компьютер': 75000, 'Термальный щит': 50000,
              'Модуль искусственной гравитации': 120000, 'Система жизнеобеспечения': 40000}

local_store = Store(items=test_list)
magic_store = Store('Чародейские Заморочки', 'Улица Волшебников, дом 17', magic_list)
space_store = Store('Космо-Комплект', 'Улица Гагарина 42', space_list)




