#!/usr/bin/python3
import random

inventory = ('Apple', 'Pineapple', 'Tomato', 'Corn', 'Strawberry',
             'Jeans', 'T-shirt', 'Shorts', 'Jacket', 'Sneakers',
             'Toothbrush', 'Shampoo', 'Shower gel', 'Detergent', 'Toothpaste',
             'Headphones', 'Charger', 'Monitor', 'Smartphone', 'TV',
             'Malone', 'Watermelon', 'Spaghetti', 'Souse', 'Pizza',
             'Hat', 'Dress', 'Blouse', 'Coat', 'Boots',
             'Razor', 'Towel', 'Hand cream', 'Mirror', 'Balm',
             'PlayStation', 'XBox', 'Speakers', 'WEB-cam', 'Camera',
             'Pan', 'Spoon', 'Fork', 'Coffee machine', 'Cup',
             'Tablecloth', 'Frying pan', 'Washcloth', 'Dishwashing liquid', 'Soap')


def bd_generator():
    q_inv = len(inventory)
    bd = []

    # Генерируем корзины покупателей так, чтобы их было не меньше 50 и не больше 100
    for c in range(random.randint(50, 100)):
        basket = []
        # В корзине может быть от 2 до 25 товаров
        for i in range(random.randint(2, 25)):
            # Случайным образом выбираем какой товар из списка кладётся в корзину
            basket.append(inventory[random.randint(0, q_inv - 1)])
        # Избавляемся от повторений
        basket = list(set(basket))
        basket.sort()
        # Добавляем полученную корзину в бд
        bd.append(basket)

    # Бд из списка переводим в кортеж
    bd = tuple(bd)
    return bd
