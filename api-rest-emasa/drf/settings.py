"""
Django settings for drf project.
Generated by 'django-admin startproject' using Django 5.1.6.
For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
from django.conf import settings
from django.conf.urls.static import static
from pathlib import Path
import os
import logging
from django.core.exceptions import ImproperlyConfigured
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY') #Poner esto en vez del de abajo para produccion

# SECURITY WARNING: don't run with debug turned on in production! cambiar DEBUG = False!!
DEBUG = False

#Colocar los dominios permitidos separados por (,) cambiar en produccion por el dominio de emasa hostinger
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')



INSTALLED_APPS = [
    #'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'rest_framework',
    #'rest_framework.authtoken',
    'api',
    'channels',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'drf.urls'

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

#WSGI_APPLICATION = 'drf.wsgi.application'
ASGI_APPLICATION = 'drf.asgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

#import dj_database_url

#NUEVA DB

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'), 
        'USER': os.environ.get('POSTGRES_USER'), 
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'), 
        'HOST': os.environ.get('POSTGRESQL_HOST'),
    }
}

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [f"redis://:{os.environ.get('REDIS_PASSWORD')}@redis:6379/0"],
        },
    },
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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

# Permitir CORS para WebSockets
MIDDLEWARE.insert(1, 'corsheaders.middleware.CorsMiddleware')

CORS_ALLOW_ALL_ORIGINS = True
#Para Produccion CORS_ALLOWED_ORIGINS = [url del frontend] #y quitar/comentar el de arriba el CORS_ALLOW_ALL

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'api.authentication.CustomTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/


STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR , 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SITE_ID =1

AUTH_USER_MODEL = "api.CustomUser" #acá es, se comenta si se usa el panel admin de django para crar users y se descomenta para usar el de api/vi/Users y conectar asì las apis

CHIRPSTACK_JWT_TOKEN = os.environ.get("CHIRPSTACK_JWT_TOKEN") #Para Produccion cambiar por el de abajo y el token ponerlo en .env.prod


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"  # Servidor de Gmail
EMAIL_PORT = 587  # Puerto para TLS  465 si es para SSL   587 si es para TLS
EMAIL_USE_TLS = True  
EMAIL_USE_SSL = False
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD") # que debe generar desde gmail, contraseña para otra aplicacio
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER