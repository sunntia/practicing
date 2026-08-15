import pandas as pd

# Создаём таблицу меню (список блюд с ценами)
menu = pd.DataFrame(
    {
        'dish_id': [1, 2, 3, 4],
        'dish_name': ['onion soup', 'green pasta', 'tomfo', 'salad'],
        'price($)': [10, 12, 7, 9]
    }
)
print('\n Таблица Меню\n')
print(menu)

# Создаём таблицу заказов (кто что заказал)
orders = pd.DataFrame(
    {
        'order_id': [101, 102, 103, 104],
        'dish_id': [3, 5, 2, 1], # Внимание: блюда с id=5 нет в меню намеренно
        'customer_name': ['John', 'Mary', 'Jeck', 'Lily']
    }
)
print('\n Таблица Заказы\n')
print(orders)

# Объединяем таблицы, чтобы увидеть все заказы и все блюда.
# outer join сохраняет все строки из обеих таблиц.
outer_join = pd.merge(menu, orders, on='dish_id', how='outer')
print('\n Общая таблица \n')
print(outer_join)

left_join = pd.merge(menu, orders, on='dish_id', how='left')
print('\nТаблица с всеми блюдами даже без заказа\n')
print(left_join)

right_join = pd.merge(menu, orders, on='dish_id', how='right')
print('\nТаблица со всеми заказами даже без блюда\n')
print(right_join)

inner_join = pd.merge(menu, orders, on='dish_id', how='inner')
print('\nТаблица только с блюдами, на которые есть заказ\n')
print(inner_join)