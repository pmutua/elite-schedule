ROOT_DIR = environ.Path(__file__) - 3  # djangohotspot/
APPS_DIR = ROOT_DIR.path('djangohotspot')  # path for django apps
 
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
 
AUTOSLUG_SLUGIFY_FUNCTION = 'slugify.slugify' # allows you to define a function for unicode-supported Slug
 
DATABASES = { 'default': env.db('DATABASE_URL', default='postgres:///djangohotspot'), }
DATABASES['default']['ATOMIC_REQUESTS'] = True # allows you to open and commit transaction when there are no exceptions. This could affect the performance negatively for traffic-heavy apps.
 
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')
ADMIN_URL = env('DJANGO_ADMIN_URL', default=r'^admin/')
 
PASSWORD_HASHERS = ['django.contrib.auth.hashers.Argon2PasswordHasher', (...)] # add this object at the beginning of the list