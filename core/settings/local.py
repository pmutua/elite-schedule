from .base import *

DATABASES['default'].update({
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'elite_schedule',
    'USER': 'pmutua',
    'PASSWORD':'kratos@2010',
    'HOST': 'localhost',
    'PORT': '',
})