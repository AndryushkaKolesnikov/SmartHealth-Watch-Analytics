# подключение библиотек
import pandas as pd
from sklearn.model_selection import train_test_split
from catboost import CatBoostRegressor
# загрузка очищенных данных
df = pd.read_csv("data/clean_smartwatch_health_data.csv")
# Разделение данных на обучающую, проверочную и тестовую выборки
train, test = train_test_split(df,train_size=0.6,random_state=42)
val, test = train_test_split(test,train_size=0.5,random_state=42)
# устанавливаем список признаков
X = ['Blood Oxygen Level (%)', 'Step Count',
       'Sleep Duration (hours)', 'Activity Level', 'Stress Level']
# установка категориальных признаков
cat_features = ['Activity Level', 'Stress Level']
# Установка целевой переменной
y = ['Heart Rate (BPM)']
# Настройка параметров модели
parameters = {'cat_features': cat_features,
              'eval_metric': 'MAPE',
              'learning_rate': 0.008,
              'random_seed':42,
              'verbose':100}
# Создаем экземпляр модели с указанными параметрами
model = CatBoostRegressor(**parameters)
# Обучение модели и оценка её качества
model.fit(train[X],train[y],eval_set=(val[X],val[y]))
# Задание новых параметров для модели
parameters = {'iterations': model.best_iteration_ + 1,
              'cat_features': cat_features,
              'eval_metric': 'MAPE',
              'learning_rate': 0.08,
              'random_seed':42,
              'verbose':100}
# Создаем экземпляр модели с указанными параметрами
model = CatBoostRegressor(**parameters)
# Объединение train и val
train_full = pd.concat([train,val])
# Обучение модели на данных из train_full
model.fit(train_full[X],train_full[y])
# Сохранение обученной модели в файл
model.save_model('data/my_model.cbm')