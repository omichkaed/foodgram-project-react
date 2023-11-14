Проект foodgram 

Онлайн-сервис и API для продуктового помощника. На сервисе можно добавлять рецепты, а 
также посмотреть рецепты других пользователей, добавить понравившиеся в избранное и список покупок.
Список покупок доступен для скачивания в текстовом формате.

Сервис размещен по адресу: https://omichfoodgram.hopto.org/. 

Данные для входа в админку.
email: admin@admin.ru
password: admin

В проекте использованы технологии:

Python 3.9
Django 3.2
Django Rest Framework 3.12.4
PostgreSQL
Docker
Gunicorn
Nginx
GitHub Actions


### Как запустить проект в контейнерах локально:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/omichkaed/foodgram-project-react.git
```

```
cd foodgram-project-react/infra
```

Установить Docker Desktop на Ваш компьютер и запустить его.

Создать директории infra файл .env и заполнить его своими данными:

```
POSTGRES_DB=foodgram_db
POSTGRES_USER=foodgram_user
POSTGRES_PASSWORD=<your_password>
DB_HOST=db
DB_PORT=5432
SECRET_KEY=<your_secret_key>
ALLOWED_HOSTS=localhost you_can_add_your_host_here
```

Запустить оркестр контейнеров:

```
docker compose up
```

Дождаться сборки и запуска всех контейнеров и в другом окне терминала выполнить миграции:

```
docker compose exec backend python manage.py migrate 
```

Собрать и скопировать статику Django:

```
docker compose exec backend python manage.py collectstatic
```
```
docker compose exec backend cp -r /app/collected_static/. /backend_static/static/ 

### Автор:

Валиуллов Илья