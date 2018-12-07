from .base import *


# Override base.py settings here 
# DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES['default'].update({
    'NAME': os.getenv('DATABASE_NAME'),
    'USER': os.getenv('DATABASE_USER'),
    'PASSWORD': os.getenv('DATABASE_PASSWORD'),
    'HOST': os.getenv('DATABASE_HOST'),
    'PORT': os.getenv('DATABASE_PORT')
})

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': 'default-locmemcache',
#         'TIMEOUT': int(os.getenv('DJNAGO_CACHE_TIMEOUT'))
#     }
# }

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.mailgun.org'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
# EMAIL_USE_TLS = True