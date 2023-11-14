Проект foodgram 

Онлайн-сервис и API для продуктового помощника. На сервисе можно добавлять рецепты, а 
также посмотреть рецепты других пользователей, добавить понравившиеся в избранное и список покупок.
Список покупок доступен для скачивания в текстовом формате.

Сервис размещен по адресу: https://omichfoodgram.hopto.org/. Полная документация к API находится в файле [docs/openapi-schema.yml](docs/openapi-schema.yml) и доступна по эндпоинту `/api/docs/`.


В проекте использованы технологии:

Python 3.11
Django 3.2
Django Rest Framework 3.12.4
PostgreSQL
Docker
Gunicorn
Nginx
GitHub Actions


Запуск проекта в Dev-режиме

Установите и активируйте виртуальное окружение
Установите зависимости из файла requirements.txt
pip install -r requirements.txt

В папке с файлом manage.py выполните команду:
python3 manage.py runserver


Запуск проекта в контейнерах

Запуск проекта с помощью docker compose
Создать директорию для проекта

В директории для проекта создать файл .env Файл .env должен содержать следующие переменные:

POSTGRES_USER=<пользователь_БД> 
POSTGRES_PASSWORD=<пароль_пользователя_БД> 
POSTGRES_DB=<имя_БД> 
DB_HOST: 127.0.0.1 
DB_PORT: 5432 
SECRET_KEY=<django-insecure-сгенерированный_на_https://djecrety.ir/_ключ_для_джанго>

Устанавливить Docker Compose, для этого поочередно выполнить команды

sudo apt update 
sudo apt install curl 
curl -fSL https://get.docker.com -o get-docker.sh sudo sh ./get-docker.sh sudo apt-get install docker-compose-plugin

Запустить Docker Compose в режиме демона

sudo docker compose -f docker-compose.production.yml up -d

Обновить git action выполнив коммит на git hub
