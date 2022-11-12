# API для Yatube
## Описание проекта
Проект позволяет обращаться к API социальной сети Yatube.
Используемые технологии:
Django - 2.2.16
Django Rest Framework - 3.12.4
Python 3.7
## Как запустить проект:
1. Клонировать репозиторий и перейти в него в командной строке:
```
git@github.com:LuckyPoRus/api_final_yatube.git
```
2. Переход в директорию с проектом:
cd kittygram
3. Cоздать и активировать виртуальное окружение:
python -m venv venv
4. Активировать виртуальное окружение:
source venv/scripts/activate
5. Оновление PIP:
python -m pip install --upgrade pip
6. Установка зависимостей используемых в проекте:
pip install -r requirements.txt
7. Выполнить миграции:
python manage.py migrate
8. Запустить проект:
python manage.py runserver

## Примеры запросов:
Получение JWT-токена:
POST
http://127.0.0.1:8000/api/v1/jwt/create/
Получить список всех публикаций:
GET
http://127.0.0.1:8000/api/v1/posts/
Добавление новой публикации:
POST
http://127.0.0.1:8000/api/v1/posts/
Получение всех комментариев к публикации:
GET
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
Получение списка доступных сообществ:
GET
http://127.0.0.1:8000/api/v1/groups/
Подписка пользователя на пользователя переданного в теле запроса:
POST
http://127.0.0.1:8000/api/v1/follow/
