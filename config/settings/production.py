from .base import *

DEBUG = False

ALLOWED_HOSTS = ['#######']

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


STATIC_ROOT = '/usr/share/nginx/html/static'

MEDIA_ROOT = '/usr/share/nginx/html/media'