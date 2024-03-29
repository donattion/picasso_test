# Тестовое задание для «Пикассо» 
### Загрузка и обработка файлов
---

### Цель:

Разработать Django REST API, который позволяет загружать файлы на сервер, а затем асинхронно обрабатывать их с использованием Celery.

---
### Требования:

1. Создать Django проект и приложение.
2. Использовать Django REST Framework для создания API.
3. Реализовать модель `File`, которая будет представлять загруженные файлы. Модель должна содержать поля:
- `file`: поле типа `FileField`, используемое для загрузки файла.
- `uploaded_at`: поле типа `DateTimeField`, содержащее дату и время загрузки файла.
- `processed`: поле типа `BooleanField`, указывающее, был ли файл обработан.

4. Реализовать сериализатор для модели `File`.
5. Создать API эндпоинт `upload/`, который будет принимать POST-запросы для загрузки файлов. При загрузке файла необходимо создать объект модели `File`, сохранить файл на сервере и запустить асинхронную задачу для обработки файла с использованием Celery. В ответ на успешную загрузку файла вернуть статус 201 и сериализованные данные файла.
6. Реализовать Celery задачу для обработки файла. Задача должна быть запущена асинхронно и изменять поле `processed` модели `File` на `True` после обработки файла.
7. Реализовать API эндпоинт `files/`, который будет возвращать список всех файлов с их данными, включая статус обработки.

---
### Используемый стек:

<pre>
Django;
DRF;
Celery;
Docker;
PostgreSQL;
Redis.
</pre>

---
### Развертывание проекта:

Создайте файл `.env` в корневой директории проекта со следующим содержимым:

<pre>
TOKEN='ВАШ_ТОКЕН'

DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432</pre>

Выполните команду для развертывания проекта:

`$ docker-compose up -d --build`

После успешного запуска выполните следующие команды:

`$ docker-compose exec django python manage.py makemigrations`

`$ docker-compose exec django python manage.py migrate`

Готово! проект доступен по адресу:

`http://localhost:5000/`

---
### API эндпоинты:

`http://localhost:5000/api/files` - список загруженных файлов.

`http://localhost:5000/api/upload` - загрузка файла.

---
