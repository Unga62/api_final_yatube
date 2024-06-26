# API для Yatube

Учебный проект Яндекс.Практикум курса Python-разработчик(backend).

## Описание
### Rest API для YaTube

YaTube - web-приложение, реализующее социальную сеть, позволяющее пользователям вести дневники, подписываться друг на друга и оставлять комментарии.

### Стек технологий

+Python
+Django
+Django REST Framework 
+Simple JWT

## Возможности

Регистрация, аутентификация (JWT) и управление учётной записью
Создание записей (постов) пользователя с возможностью загрузки изображения
Создания комментарием к постам пользователей
Подписка на записи выбранных авторов
Реализованы кеширование и паджинация

# Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Unga62/api_final_yatube.git
```

```
cd kittygram_backend
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

После запуска проекта, документация будет доступна по адресу:

```
http://127.0.0.1:8000/redoc/
```

### Автор

Ильин Даниил, email: danil.ili@yandex.ru