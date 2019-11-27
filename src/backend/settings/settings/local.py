import os
from . import base

ALLOWED_HOSTS = ['*']
# INSTALLED_APPS = base.INSTALLED_APPS + ['django_extensions']
STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(base.BASE_DIR, 'static'),
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(base.BASE_DIR, 'media')
