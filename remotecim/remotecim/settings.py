from pathlib import Path
import os

ALLOWED_HOSTS = ['127.0.0.1']

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

AUTH_USER_MODEL = 'remotecim.Usuario'


BASE_DIR = Path(__file__).resolve().parent.parent

CONNECTION_IP1 = '127.0.0.1'
#CONNECTION_IP1 = '192.168.0.41'
CONNECTION_IP2 = '192.168.0.42'
CONNECTION_IP3 = '192.168.0.43'
PUERTO_SOCKET = 12345

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DEBUG = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
    'remotecim',
]

LANGUAGE_CODE = 'en-us'

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROLES = {
    'ADMINISTRADOR': 'administrador',
    'PROFESOR': 'profesor',
    'ESTUDIANTE': 'estudiante',
}

ROOT_URLCONF = 'remotecim.urls'

SECRET_KEY = 'django-insecure-@@6g^)_9dx&+c+hfaljt1tee8-^ks=t3m1=s3fy8_d9hi955)g'

STATIC_URL = '/static/'

STATICFILES_DIRS = os.path.join(BASE_DIR, 'remotecim/static'),

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['remotecim/templates'], # considerar que esta ruta debe estar al nivel de 'manage.py'
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

TIME_ZONE = 'America/Santiago'

USE_I18N = True

USE_TZ = True

WSGI_APPLICATION = 'remotecim.wsgi.application'


