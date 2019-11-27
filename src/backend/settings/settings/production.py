
# Abdulaziz//Alfuhigi abajall@gmail.com
import os
from . import base
from decouple import config

ALLOWED_HOSTS = ['*']


base.DATABASES['default'] = {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': config('DB_NAME'),
    'USER': config('DB_USER'),
    'PASSWORD': config('DB_PASSWORD'),
    'HOST': config('DB_HOST'),
    'PORT': config('DB_PORT'),
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(base.BASE_DIR, 'static')
# STATICFILES_DIRS = [
#     os.path.join(base.BASE_DIR, 'static'),
# ]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(base.BASE_DIR, 'media')
