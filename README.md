# SmartHealth-Watch-Analytics
Репозиторий посвящен анализу и обработке данных с умных часов, включая такие показатели, как сердечный ритм, уровень кислорода в крови, количество шагов, продолжительность сна, уровень активности и стресса.
<!--Блок информации о репозитории в бейджах-->
![GitHub top language](https://img.shields.io/github/languages/top/AndryushkaKolesnikov/SmartHealth-Watch-Analytics)
![GitHub](https://img.shields.io/github/license/AndryushkaKolesnikov/SmartHealth-Watch-Analytics)
![GitHub Repo stars](https://img.shields.io/github/stars/AndryushkaKolesnikov/SmartHealth-Watch-Analytics)
![GitHub issues](https://img.shields.io/github/issues/AndryushkaKolesnikov/SmartHealth-Watch-Analytics)
![GitHub last commit](https://img.shields.io/github/last-commit/AndryushkaKolesnikov/SmartHealth-Watch-Analytics)
[![Discussion](https://img.shields.io/badge/Discuss-Issues-blue?logo=github)](https://github.com/AndryushkaKolesnikov/SmartHealth-Watch-Analytics/issues/new/choose)
<!--Установка-->
## Установка (Linux)
У вас должны быть установлены [зависимости проекта](https://github.com/AndryushkaKolesnikov/SmartHealth-Watch-Analytics#зависимости)

1. Клонирования репозитория
   
   ```git clone https://github.com/AndryushkaKolesnikov/SmartHealth-Watch-Analytics.git```
2. Переход в директорию SmartHealth-Watch-Analytics
   
   ```cd SmartHealth-Watch-Analytics```
   
4. Создание виртуального окружения

   ```python3 -m venv venv```

4. Активация виртуального окружения

   ```source venv/bin/activate```

5. Установка зависимостей

   ```pip3 install -r requirements.txt```

6. Запуск файла

   ```jupyter notebook --execute smartwatch.ipynb```
<!--Поддержка-->
## Поддержка
Если у вас возникли сложности или вопросы по использованию пакета, создайте 
[обсуждение](https://github.com/AndryushkaKolesnikov/SmartHealth-Watch-Analytics/issues/new/choose) в данном репозитории или напишите на электронную почту <kolesnikow.andrei13@gmail.com>.

<!--зависимости-->
## Зависимости
Эта программа зависит от интепретатора Python версии 3.7.9 или выше, PIP 20.1.1 или выше.
### Версии библиотек необходимые для запуска
| Название              |  Версия     |
|-----------------------|-------------|
| **numpy**             | 2.2.4       |
| **pandas**            | 2.2.3       |
| **python-dateutil**   | 2.9.0.post0 |
| **ipykernel**         | 6.0.0       |
| **pytz**              | 2025.2      |
| **six**               | 1.17.0      |
| **tzdata**            |  2025.2     |
