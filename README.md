# django tailapinex  
<img width="1070" alt="django+tailwindcss+alpine.js+htmx" src="https://user-images.githubusercontent.com/30228894/188502285-d2c5d44b-8729-4aa0-bbe1-4e1ebc623ff3.png">


This project is a template for django projects with the use of:
* [django](https://www.djangoproject.com)
* [tailwindcss](https://tailwindcss.com) with [django-tailwind](https://github.com/timonweb/django-tailwind/blob/master/docs/installation.md)
* [alpine.js](https://alpinejs.dev)
* [htmx](https://htmx.org) with [django-htmx](https://github.com/adamchainz/django-htmx)

## Get started
The packages are organized with [poetry](https://python-poetry.org). For instructions how to use it, see their documentation.

1. To install all the necessary packages run `poetry update`
2. After that you can start the tailwind-watcher with `poetry run python manage.py tailwind start`
3. In a second terminal run the Django server with `poetry run python manage.py runserver`

Open [`http://127.0.0.1:8000/htmx`](http://127.0.0.1:8000/htmx) to see it working :)
