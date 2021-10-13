from .base import *

#Use the following live settings to build on Travis CI

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': os.environ['DATABASE_NAME'],
    'USER': os.environ['DATABASE_USER'],
    'PASSWORD': os.environ['DATABASE_PASSWORD'],
    }
}