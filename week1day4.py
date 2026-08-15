import pandas as pd

df = pd.read_csv('titanic/train.csv') #читаем файл
# df.isnull().sum() - Найти пропуски
df['Age']= df['Age'].fillna(df['Age'].mean()) #Заполнить пропуски в `Age` средним значением
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0]) #Заполнить пропуски в `Embarked` модой
df = df.drop('Cabin', axis=1) #Удалить столбец `Cabin` (слишком много пропусков)
df = df.drop_duplicates() #Удалить дубликаты

#Создать новую колонку `AgeGroup` (0-18, 19-30, 31-50, 50+)
bins = [0, 18, 30, 50, 100] 
labels = ['0-18', '19-30', '31-50', '50+'] 
df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels, right=True) 

# Группируем данные по полу (мужчины/женщины), 
# берем колонку 'Survived' и считаем среднее значение (процент выживших) для каждой группы.
df.groupby('Sex')['Survived'].mean()

# Группируем данные по классу билета (1-й, 2-й, 3-й),
# берем колонку 'Survived' и считаем среднее значение (процент выживших) в каждом классе.
df.groupby('Pclass')['Survived'].mean()

# Агрегируем (собираем) данные по классам билета.
# Для каждой группы (1-й, 2-й, 3-й класс) считаем:
# - средний возраст пассажиров (Age → mean)
# - общую сумму, которую заплатили все пассажиры этого класса (Fare → sum)
# Это позволяет увидеть социально-экономический портрет каждого класса.
df.groupby('Pclass').agg({'Age': 'mean', 'Fare': 'sum'})

# Строим сводную таблицу: матрицу выживаемости по двум признакам.
# - Строки (index) — пол пассажира.
# - Столбцы (columns) — класс билета.
# - Значение (values) — процент выживших.
# Таблица наглядно показывает, что женщины 1-го класса имели наибольший шанс на спасение.
pd.pivot_table(df, values='Survived', index='Sex', columns='Pclass')

print(pd.pivot_table(df, values='Survived', index='Sex', columns='Pclass'))

