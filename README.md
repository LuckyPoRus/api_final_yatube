# api_final_yatube

Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
git@github.com:LuckyPoRus/api_final_yatube.git
Переход в директорию с проектом:
cd kittygram
Cоздать и активировать виртуальное окружение:
python -m venv venv
Активировать виртуальное окружение:
source venv/scripts/activate
Оновление PIP:
python -m pip install --upgrade pip
Установка зависимостей используемых в проекте:
pip install -r requirements.txt
Выполнить миграции:
python manage.py migrate
Запустить проект:
python manage.py runserver
