# Django App

App based on Python [Django web Framework](https://www.djangoproject.com/)

![example workflow](https://github.com/anishst/django_app/actions/workflows/python-app.yml/badge.svg)

## Current Apps

- Blog

## Setup

1. create virtual env (windows): ```python -m venv env```
2. activate env: ```.\env\Scripts\activate```
3. install requirement: ```pip install -r requirements.txt```
4. create super user: ```python manage.py createsuperuser```
4. do migrations: ```python manage.py migrate```
5. run app: ```python manage.py runserver```


## Shell Usage

1. enter db shell: ```python manage.py dbshell``
    - if command doesn't work, make sure sqlie3 exe in path var: https://www.sqlite.org/download.html
    - commands
        - to see tables: ```.tables```
        - see schema: ```.schema tablename```

## Tasks

- [x] Setup basic Django project
- [x] add basic blog
- [x] add CRUD features
- [ ] add favorite star icon to turn on/off
- [ ] add tasks model
- [x] add search feature
- [ ] add pagination
- [ ] add ckeditor for rich text editing
    - ```pip install django-ckeditor``` 
    - requires migration after changes and add to settings.py under INSTALLED_APPS
    - add RichTextField to forms
- [ ] [try crispy forms](https://simpleisbetterthancomplex.com/tutorial/2018/08/13/how-to-use-bootstrap-4-forms-with-django.html)
- [ ] add [tests](https://docs.djangoproject.com/en/3.1/intro/tutorial05/#introducing-automated-testing)
        - https://docs.djangoproject.com/en/3.1/internals/contributing/writing-code/unit-tests/
- [ ] containerize?
- [x] use github actions `````.github\workflows\python-app.yml`````
    - [x] added build status icon

## Running Tests

1. blog tests: ```python manage.py test blog```

## Running using pytest
1. pytest

## Docker Practice

### Using Dockerfile

1. build : ```docker build --tag python-django .```
2. run: ```docker run --name djangoapp --publish 8000:8000 python-django```
3. apply migration by logging into container: ```docker exec -it djangoapp /bin/bash ```
