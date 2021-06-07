"""
Django settings for simplesite project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent # путь к папке проекта, вычисляется автоматически


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '20(of=1f!-g+!5m=6mct36le765&nrq&wb5zys*04)&*rejh^l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # режим работы сайта

ALLOWED_HOSTS = []


# Application definition
# список приложений зарегистр в проекте
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth', # встроенная система разграниченого доступа
    'django.contrib.contenttypes', # хранит списов всех моделей
    'django.contrib.sessions', # обрабатывает серверные сессии
    'django.contrib.messages', # выводит всплывающиеся сообщения
    'django.contrib.staticfiles', # обрабатывает статические файлы
    'bboard.apps.BboardConfig',
    'rest_framework', #Rest api репрезентативная передача состояния
    'corsheaders', # Инф с другого домена
]
# посредник - обработка клиентского запроса перед передачей контролеру и его выполнением
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware', # доп защита от хакер отак
    'django.contrib.sessions.middleware.SessionMiddleware', # обрабатывает сервер на низком уровне
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware', # учавствует в преварительной обработке запроса
    'django.middleware.csrf.CsrfViewMiddleware', # защита методом ПОСТ
    'django.contrib.auth.middleware.AuthenticationMiddleware', # хранит текущего пользователя
    'django.contrib.messages.middleware.MessageMiddleware', # обработка смс на низком уровне
    'django.middleware.clickjacking.XFrameOptionsMiddleware', # доп защита от сетевых атак
]

ROOT_URLCONF = 'simplesite.urls' # указывает путь к модулю где записанны все ЮРЛЫ

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [], #список путей в которых шаблонизатор будет искать шаблоны
        'APP_DIRS': True, #если ТРУ то будет искать шаблоны в папке templates
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug', #хранит значение параметра ДЕБАГ
                'django.template.context_processors.request',#добавляет в контекст шаблона переменную хранящую обьект текущего запроса
                'django.contrib.auth.context_processors.auth',#хранит инф про пользователя и его правах
                'django.contrib.messages.context_processors.messages',#
            ],
        },
    },
]

WSGI_APPLICATION = 'simplesite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True # перевод на язык который указан в  LANGUAGE_CODE

USE_L10N = True

USE_TZ = True # хранит дату


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

LOGIN_URL='/account/login/' #интернет адрес на который будет выполнено перенаправлени после попытки зайти без логина

LOGIN_REDIRECT_URL='/' #адресс перенаправления после успешного логина

LOGOUT_REDIRECT_URL='/'
