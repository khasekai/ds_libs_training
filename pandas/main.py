# Смотри https://habr.com/ru/company/ruvds/blog/494720/

import pandas as pd

# Загрузка CSV-данных
anime = pd.read_csv("anime.csv")
rating = pd.read_csv("rating.csv")
anime_modified = anime.set_index("name")

# Создание датафрейма вручную
df = pd.DataFrame({'Column1': [1, 2, 3], 'Column2': ['1', '2', '3']})

# Копирование датафрейма
anime_copy = anime.copy(deep=True)  # When deep=False, only references to the data and index are copied.
                                    # Any changes to the data of the original will be reflected in the shallow copy.

# Экспорт в CSV
rating[:10].to_csv('rating_copy.scv', index=False)

# Получение n записей из начала или конца датафрейма
anime_copy.head(3)
rating.tail(5)

# Подсчёт количества строк в датафрейме
len(df)

# Подсчёт количества уникальных значений в столбце
len(rating['user_id'].unique())

# Получение сведений о датафрейме
# anime.info()

# Вывод статистических сведений о датафрейме
rating.describe()

# Подсчёт количества значений в столбцах
anime.type.value_counts()

# Создание списка или объекта Series на основе значений столбца
anime['genre'].tolist()

# Получение списка значений из индекса
anime.index.tolist()

# Получение списка значений столбцов
anime.columns.tolist()

# Присоединение к датафрейму нового столбца с заданным значением
anime['Train set'] = True

# Создание нового датафрейма из подмножества столбцов
subdf = anime[['name', 'episodes']]

# Удаление заданных столбцов
anime.drop(['anime_id', 'genre', 'members'], axis=1).head() # if axis=0 drops rows, not columns

# Добавление в датафрейм строки с суммой значений из других строк
df = pd.DataFrame([[1,'Bob', 8000],
                  [2,'Sally', 9000],
                  [3,'Scott', 20]], columns=['id','name', 'power level'])
df.append(df.sum(axis=0), ignore_index=True)

# Конкатенация двух датафреймов
df1 = anime[0:2]
df2 = anime[2:4]
df = pd.concat([df1, df2], ignore_index=True)

# Слияние датафреймов
rating.merge(anime, left_on='anime_id', right_on='anime_id', suffixes=('_left', '_right'))
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html

# Получение строк с нужными индексными значениями
anime_modified.loc[['Haikyuu!! Second Season','Gintama']]

# Получение строк по числовым индексам
anime_modified.iloc[0:3]

# Получение строк по заданным значениям столбцов
anime[anime['type'].isin(['TV', 'Movie'])]
anime[anime['type'] == 'TV']

# Получение среза датафрейма
anime[1:3]

# Фильтрация по значению
[anime[anime['rating'] > 8]]

# Сортировка
anime.sort_values('rating', ascending=False)

# Функция df.groupby и подсчёт количества записей
anime.groupby('type').count()

# Функция df.groupby и агрегирование столбцов различными способами
anime.groupby(["type"]).agg({
  "rating": "sum",
  "episodes": "count",
  "name": "last"
}).reset_index()

# Создание сводной таблицы
tmp_df = rating.copy()
tmp_df.sort_values('user_id', ascending=True, inplace=True)
tmp_df = tmp_df[tmp_df.user_id < 10]
tmp_df = tmp_df[tmp_df.anime_id < 30]
tmp_df = tmp_df[tmp_df.rating != -1]
pd.pivot_table(tmp_df, values='rating', index=['user_id'], columns=['anime_id'], aggfunc=np.sum, fill_value=0)

# Запись в ячейки, содержащие значение NaN, какого-то другого значения
pivot = pd.pivot_table(tmp_df, values='rating', index=['user_id'], columns=['anime_id'], aggfunc=np.sum)
pivot = pivot.fillna('0')

# Отбор случайных образцов из набора данных
anime.sample(frac=0.25)

# Перебор строк датафрейма
for idx,row in anime[:2].iterrows():
    print(idx, row)
