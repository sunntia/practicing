import pandas as pd # Для работы с таблицами (DataFrame)
import numpy as np # Для генерации случайных чисел

# Устанавливаем зерно для воспроизводимости (чтобы у всех были одинаковые данные)
np.random.seed(42)

# Генерируем 100 записей о продажах
data = {
    'sale_date': pd.date_range(start='2024-01-01', periods=100, freq='D'),  # Даты с 1 января 2024
    'store_id': np.random.randint(1, 6, 100),  # 5 магазинов (1-5)
    'category': np.random.choice(['Electronics', 'Clothing', 'Food', 'Books'], 100),
    'revenue': np.random.randint(100, 1000, 100),
    'quantity': np.random.randint(1, 20, 100)
}

df = pd.DataFrame(data)

# Функция принимает число (revenue) и возвращает строку с названием категории.
# Это классическая "ступенчатая" логика (if-elif-else).
def category(revenue):
    if revenue < 300:
        return 'Low'
    elif 300 <= revenue <= 700:
        return 'Medium'
    else:
        return 'High'

# Создаём новую колонку revenue_category.
# Для каждого значения в колонке revenue вызывается функция category(),
# которая возвращает соответствующую категорию (Low/Medium/High).
df['revenue_category'] = df['revenue'].apply(category)

# Выводим первые 10 строк таблицы, но только две колонки:
# - revenue (числовое значение выручки)
# - revenue_category (категория, которую мы только что создали)
#print(df[['revenue', 'revenue_category']].head(10))

# Выводим, сколько продаж попало в каждую категорию (Low / Medium / High).
# value_counts() считает количество уникальных значений в колонке.
#print(df['revenue_category'].value_counts())

# Функция принимает дату и возвращает полное название месяца (January, February, ...).
# .strftime('%B') — метод форматирования даты в строку.
def month_name(sale_date):
    return sale_date.strftime('%B')

# Применяем функцию к колонке sale_date.
df['month_name'] = df['sale_date'].apply(month_name)
#print(df[['sale_date', 'month_name']].head(10))

# Создаём словарь для замены полных названий категорий на их сокращения.
# Это стандартная практика для уменьшения длины текстовых значений.
cat_dict = {
    'Electronics': 'E',
    'Clothing': 'C', 
    'Food': 'F', 
    'Books': 'B'
}

# .map() — заменяет значения по словарю (быстрее и проще, чем apply).
# Вместо 'Electronics' теперь будет стоять 'E'.
df['category_short'] = df['category'].map(cat_dict)
#print(df[['category', 'category_short']].head(10))

# Создаём словарь для замены числовых ID магазинов на их названия.
id_dict = {
    1: 'North',
    2: 'South',
    3: 'East',
    4: 'West',
    5: 'Central'
}

# .map() — заменяет числа на названия из словаря.
df['new_store_id'] = df['store_id'].map(id_dict)
print(df[['store_id', 'new_store_id']].head(10))