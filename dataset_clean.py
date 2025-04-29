# подключение библиотеки pandas
import pandas as pd
import numpy as np
# читаем исходный DataFrame (df) из файла
df = pd.read_csv("data/unclean_smartwatch_health_data.csv")

# Функция для нормализации значений в столбце Activity Level
def activity_level_group(x):
  if x in ['Highly_Active', 'Highly Active']:    # исправляем опечатки
    return 'Highly Active'                       # и
  if x in ['Seddentary', 'Sedentary']:           # приводим  к общему 
    return 'Sedentary'                           # виду значения в столбце
  if x in ['Actve', 'Active']:
    return 'Active'
  return x
# Вызываем функцию для нормализации значений
df['Activity Level'] = df['Activity Level'].apply(activity_level_group)

# разделяем DataFrame на группы на основе значений в столбце 'Activity Level'
df['Blood Oxygen Level (%)'] = df.groupby(['Activity Level'],
                                     # заменяем пропуски средним значением для каждой группы
                                          dropna=False)['Blood Oxygen Level (%)'].transform(lambda x: x.fillna(x.mean()))

# разделяем DataFrame на группы на основе значений в столбцах 'Activity Level', 'Stress Level'
# и 'Sleep Duration (hours)'
df['Heart Rate (BPM)'] = df.groupby(['Activity Level','Stress Level'],
                                     # заменяем пропуски средним значением для каждой группы
                                          dropna=False)['Heart Rate (BPM)'].transform(lambda x: x.fillna(x.mean()))

# разделяем DataFrame на группы на основе значений в столбце 'Activity Level'
df['Step Count'] = df.groupby(['Activity Level'],
                                     # заменяем пропуски средним значением для каждой группы
                                          dropna=False)['Step Count'].transform(lambda x: x.fillna(x.mean()))

# Заменяем все пропуски в столбце User ID случайными числами
df["User ID"] = df['User ID'].transform(lambda x: np.random.rand())

# Преобразование столбца Sleep Duration (hours) в числовой формат
df['Sleep Duration (hours)'] = pd.to_numeric(df['Sleep Duration (hours)'], downcast="float", errors='coerce') 
# разделяем DataFrame на группы на основе значений в столбцах 'Activity Level' и 'Stress Level'
df['Sleep Duration (hours)'] = df.groupby(['Activity Level','Stress Level'],
                                          dropna=False)['Sleep Duration (hours)'].transform(lambda x: x.fillna(x.mean()))

# Удаляем отсутствующие значения в остальных столбцах
df = df.dropna()
# сохраняем очищенный DataFrame(df) в файл
df.to_csv("data/clean_smartwatch_health_data.csv", encoding='utf-8', index=False, header=True)