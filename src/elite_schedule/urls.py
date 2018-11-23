from django.conf.urls  import include,url

from . import views

app_name = "elite_schedule"

urlpatterns = [
    url('', views.index, name='index'),
]