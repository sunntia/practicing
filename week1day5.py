import pandas as pd
import numpy as np

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

# Смотрим, что получилось
#print("Первые 5 строк:")
#print(df.head())
#print("\nИнформация о колонках:")
#print(df.info())

df['year'] = pd.to_datetime(df['sale_date']).dt.year
df['month'] = pd.to_datetime(df['sale_date']).dt.month
df['day_of_week'] = pd.to_datetime(df['sale_date']).dt.dayofweek

# Смотрим, что получилось
#print(df['year'])
#print(df['month'])
#print(df['day_of_week'])

# print(df[['sale_date', 'year', 'month', 'day_of_week']].head(10))

sales_by_day = df.groupby('day_of_week')['sale_date'].count()
max_day = sales_by_day.idxmax()
print(f'День с максимальным числом продаж: {max_day}')


