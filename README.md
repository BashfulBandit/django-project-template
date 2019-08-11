# Django Project Template

This simple Django Project Template is based off the default Django Project Template
with some additional environment variables and a core app for a simple home page.
It includes a Gunicorn config file to help with deploying using Gunicorn. I mainly
use this for development in a Docker image.

See [BashfulBandit's docker-django](https://github.com/BashfulBandit/docker-django) for more information.

## What is Django?

Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

> <a href="https://en.wikipedia.org/wiki/Django_(web_framework)">Django Wikipedia</a>

## Getting Started

These instructions will get you a copy of the project up and running on your local
machine for development and testing purposes.

```
$ django-admin startproject
    --template https://github.com/BashfulBandit/django-project-template/archive/v2.2.zip
    <project_name>

$ cd <project_name>
$ python3 manage.py runserver 127.0.0.1:8000
```

You can now visit the base home page at http://localhost:8000

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Gunicorn](https://gunicorn.org/) - Python WSGI used to make deploying with a web server easy.

## Deploy with Gunicorn

```
$ django-admin startproject
    --template https://github.com/BashfulBandit/django-project-template/archive/v2.2.zip
    <project_name>

$ cd <project_name>
$ gunicorn --config config.py <project_name>.wsgi:application
```

You can now visit the base home page at http://localhost:8000

## Environment Variables

Because I mainly used this in a Docker image, I have designed the `<project_name>/settings.py`
with some environment variables to make development in the Docker environment and
deploying into a production environment easier. This is a list of environment variables
it uses. It is fine if you don't define these Environment Variables because there are
default values for the Django variables which use the Environment variables.

### `HOST`

This environment variable is used to set the Django ALLOWED_HOSTS array. It has
a default value of `*`.

https://docs.djangoproject.com/en/2.1/ref/settings/#allowed-hosts

### `SECRET_KEY`

This environment variable is used to set the Django SECRET_KEY variable.
Default value is the secret key generated by Django when making the project.
The default value shouldn't be used in a production environment. See below for
more information.

https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-SECRET_KEY

### `DEBUG`

This environment variable is used to set the Django DEBUG variable. It has a
default value of `True`.

https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-DEBUG

### `SQL_ENGINE`

This environment variable is used to set the Django ENGINE variable for the default
Database in the DATABASES array. It has a default value of `django.db.backends.sqlite3`.

https://docs.djangoproject.com/en/2.1/ref/settings/#databases

### `MYSQL_DATABASE`

This environment variable is used to set the Django NAME variable for the default
Database in the DATABASES array. It has a default value of `db.sqlite3`.

https://docs.djangoproject.com/en/2.1/ref/settings/#databases

### `MYSQL_USER`

This environment variable is used to set the Django USER variable for the default
Database in the DATABASES array. It has a default value of `django`.

https://docs.djangoproject.com/en/2.1/ref/settings/#databases

### `MYSQL_PASSWORD`

This environment variable is used to set the Django PASSWORD variable for the
default Database in the DATABASES array. It has a default value of `password`,
but it shouldn't be used in a production environment.

https://docs.djangoproject.com/en/2.1/ref/settings/#databases

### `MYSQL_HOST`

This environment variable is used to set the Django HOST variable for the default
Database in the DATABASES array. It has a default value of `localhost`.

https://docs.djangoproject.com/en/2.1/ref/settings/#databases

### `MYSQL_PORT`

This environment variable is used to set the Django PORT variable for the default
Database in the DATABASES array. It has a default value of `3306`.

https://docs.djangoproject.com/en/2.1/ref/settings/#databases
