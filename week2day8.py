#ПРОЕКТ: База данных "Покупатели и заказы"
# Описание: Создаёт и заполняет две связанные таблицы:
#           users (пользователи) и orders (заказы).

import sqlite3 as sl

# Подключаемся к базе данных (если файла нет — он создастся автоматически)
con = sl.connect('thecode2.db')

# Проверяем, существует ли таблица users
# sqlite_master — системная таблица, где хранится информация обо всех объектах БД
with con:
    data = con.execute("select count(*) from sqlite_master where type='table' and name='users'")
    for row in data:
        if row[0] == 0: # Если таблицы нет (count = 0)
            with con:
                con.execute("""
                    create table users (
                    id integer primary key,
                    name varchar(20),
                    age integer,
                    email varchar(20)
                    );
                """)

# Подготавливаем SQL-запрос для вставки или обновления пользователей
# INSERT OR REPLACE — если пользователь с таким id уже есть, он обновится,
# если нет — добавится новый.
sql = "insert or replace into users (id, name, age, email) values (?, ?, ?, ?)"

# Данные пользователей: список кортежей (id, name, age, email)
data = [
    (100, 'John M', 20, 'john@mail.ru'),
    (101, 'Kim T', 16, 'kim@mail.ru'),
    (102, 'Katie L', 30, 'katie@mail.ru'),
    (103, 'Noah H', 45, 'noah@mail.ru'),
    (104, 'Miley F', 34, 'miley@mail.ru'),
    (105, 'Patrick L', 25, 'patrick@mail.ru'),
    (106, 'Sam W', 20, 'sam@mail.ru'),
    (107, 'Sally B', 19, 'sally@mail.ru'),
    (108, 'Lora T', 21, 'lora@mail.ru'),
    (109, 'Ken D', 24, 'ken@mail.ru'),
]

# Вставляем всех пользователей одной командой (executemany)
with con:
    con.executemany(sql, data)

# Выводим всех пользователей, отсортированных по имени (для наглядности)
with con:
    data = con.execute("select * from users order by name")
    for row in data:
        print(row)

# Проверяем, существует ли таблица orders
with con:
    data = con.execute("select count(*) from sqlite_master where type='table' and name='orders'")
    for row in data:
        if row[0] == 0:
            with con:
                con.execute("""
                    create table orders (
                    order_id integer primary key autoincrement,
                    user_id integer,
                    product text,
                    price integer,
                    foreign key (user_id) references users(id)
                    );
                """)

# Данные заказов: список кортежей (user_id, product, price)
# Обрати внимание: order_id не указываем — он будет создан автоматически
orders_data = [
    (100, 'Laptop', 1200),
    (100, 'Mouse', 25),
    (101, 'Keyboard', 80),
    (102, 'Monitor', 300),
    (103, 'Phone', 600),
    (103, 'Case', 20),
    (105, 'Tablet', 400),
    (107, 'Headphones', 150),
    (108, 'Charger', 30),
    (999, 'USB Cable', 10) # Этот пользователь отсутствует в таблице users (для проверки JOIN)
]

# Вставляем заказы
with con:
    # 1. Удаляем все старые заказы, чтобы избежать дубликатов
    con.execute("DELETE FROM orders;")
    # 2. Вставляем новые заказы
    # INSERT OR REPLACE — если запись с таким user_id и product уже существует,
    # она обновится; если нет — добавится новая
    con.executemany('INSERT INTO orders (user_id, product, price) VALUES (?, ?, ?)', orders_data)

# Выводим все заказы
with con:
    orders_data = con.execute("select * from orders")
    for row in orders_data:
        print(row)

# Выводим заказы вместе с именами покупателей
# JOIN связывает таблицы по условию: users.id = orders.user_id
with con:
    data = con.execute("""
    select users.name, orders.product, orders.price
    from users
    join orders on users.id = orders.user_id
    """)
    print("\nЗаказы с покупателями:")
    rows = data.fetchall() # Извлекаем все строки результата
    for row in rows:
        print(row)

# Закрываем соединение с базой данных, чтобы освободить ресурсы
con.close()
print("\nУспешно выполнено!")