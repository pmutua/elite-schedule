from .base import *

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
INSTALLED_APPS += ['debug_toolbar', ]
DEBUG_TOOLBAR_CONFIG = { 
  'DISABLE_PANELS': [ 'debug_toolbar.panels.redirects.RedirectsPanel', ],
  'SHOW_TEMPLATE_CONTEXT': True,
}

INTERNAL_IPS = ['127.0.0.1']

INSTALLED_APPS += ['django_extensions', ]
