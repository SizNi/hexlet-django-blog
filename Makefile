new_project: # создание джанго-проект
	#django-admin startproject hexlet_django_blog .

new_app:
	#django-admin startapp app_name

dev:
	python3 manage.py runserver

create_model: # Миграция (сообщаем джанго, что создали новую модель в models.py)
	python manage.py makemigrations

migration: # заводим модель в базу данных (название модели и ее номер)
	python manage.py sqlmigrate article 0001

commit_migration: # подтверждаем миграцию (как push в гите после коммита)
	python manage.py migrate

