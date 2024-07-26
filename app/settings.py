import os
from pathlib import Path

import dj_database_url
from prettyconf import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config(
    "SECRET_KEY",
    default="django-insecure-*z=*hnnmq@g(5w3$%bj_*3ni_i$gbr(xl^k0hl!lt1dhcrg)u0",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=False, cast=config.boolean)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=config.list)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # third party app's
    'rest_framework',
    'corsheaders',
    'drf_yasg',
    # app´s
    'app.core',
    'app.people'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'


# Database
DATABASE_URL = config("DATABASE_URL")
DATABASES = {"default": dj_database_url.parse(DATABASE_URL)}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Fortaleza"
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
PROJECT_FOLDER = os.path.dirname(os.path.dirname(__file__))
STATIC_ROOT = os.path.join(
    os.path.join(os.path.join(PROJECT_FOLDER, "resources", "static"))
)
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(
    os.path.join(os.path.join(PROJECT_FOLDER, "resources", "media"))
)
MEDIA_URL = "/media/"
COMPRESS_ROOT = STATIC_ROOT

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field


CORS_ALLOWED_ORIGINS = config(
    "CORS_ALLOWED_ORIGINS",
    default=[
        "http://localhost:4200",
    ],
    cast=config.list,
)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
