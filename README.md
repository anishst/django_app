# Django App

App based on Python [Django web Framework](https://www.djangoproject.com/)

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

## Running Tests

1. blog tests: ```python manage.py test blog```

## Running using pytest
1. pytest


## Resources:
- [Django official page](https://www.djangoproject.com/)
- [Tutorial](https://docs.djangoproject.com/en/3.1/intro/tutorial01/)
- Video tutorials
    - [codemy blog app](https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi)
    - [codemy stock app](https://www.youtube.com/watch?v=iu3V4cOJW4I&list=PLCC34OHNcOtqNxahjUPo2BPC2qrVNawYK)
    - [corey](https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)
- [VS Code Setup](https://code.visualstudio.com/docs/python/tutorial-django)
- [VS Code plugins](https://morioh.com/p/b6323e6cdfca)
    - [Djaneiro - Django Snippets](https://marketplace.visualstudio.com/items?itemName=thebarkman.vscode-djaneiro)
        - var = {{}}
        - block
- [random text gen](https://www.lipsum.com/)
- Queries
    - [DB Q](https://docs.djangoproject.com/en/3.1/topics/db/queries/)
- Testing
    - [Django Testing Playlist](https://www.youtube.com/watch?v=qwypH3YvMKc&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM)
    - [Testing Tools](https://docs.djangoproject.com/en/3.1/topics/testing/tools/)
- Examples:
    - [Blog Example](https://djangocentral.com/building-a-blog-application-with-django/)    
    - [Dockerizing Django with Postgres, Gunicorn, and Nginx](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/)


## KNown issues

1. RuntimeError: Database access not allowed, use the "django_db" mark
fix add marker to pytests