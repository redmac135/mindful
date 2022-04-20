from .defaults import *
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')
CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS')

DATABASES = {}
DATABASES['default'] = dj_database_url.config()

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO','https')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')