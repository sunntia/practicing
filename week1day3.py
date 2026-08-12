import pandas as pd

df = pd.read_csv('titanic/train.csv') #считывание файла train.csv
print(df.head(5)) #вывод первых 5 строк
print(df.info()) #вывод информации о файле
print(df.dtypes) #вывод типов данных
print(df.describe()) #описание всех столбцов


print(df[df['Age'] > 30]) #выбор всех строк, где возраст больше 30
print(df.loc[1, 'Age']) #выбор значения первой строки столбца Age
print(df.iloc[1, 5]) #выбор значения первой строки столбца Sex

print(df['Age']) #выбор столбца Age
print(df['Age'].min()) #минимальное значение столбца Age
print(df['Age'].max()) #максимальное значение столбца Age
print(df['Age'].mean()) #среднее значение столбца Age
print(df['Age'].describe()) #описание столбца Age
