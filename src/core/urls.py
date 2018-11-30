"""soccerstat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls import include,url
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_jwt.views import refresh_jwt_token

schema_view = get_schema_view(
   openapi.Info(
      title="Elite Schedule API",
      default_version='v1',
      description="API providing historical results & odds to help soccer betting enthusiasts",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="pmutua@live.com"),
      license=openapi.License(name="BSD License"),
   ),
   validators=['flex', 'ssv'],
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url('admin/', admin.site.urls),
    # adding '' results to redirecting to root 
    url('api/elite_schedule/', include('elite_schedule.urls')),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # TODO leave this with '' to start as root
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # change redoc to  '' 
    url(r'^refresh-token/', refresh_jwt_token),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns



# if settings.DEBUG:
#      urlpatterns += [
#           url(r'^400/$',
#               default_views.bad_request,
#               kwargs={'exception': Exception('Bad Request!')}),
#           url(r'^403/$',
#               default_views.permission_denied,
#               kwargs={'exception': Exception('Permission Denied')}),
#           url(r'^404/$',
#               default_views.page_not_found,
#               kwargs={'exception': Exception('Page not Found')}),
#           url(r'^500/$',
#               default_views.server_error),
#      ]
# if 'debug_toolbar' in settings.INSTALLED_APPS:
#      import debug_toolbar
#           urlpatterns = [
#           url(r'^__debug__/', include(debug_toolbar.urls)),
# ] + urlpatterns
