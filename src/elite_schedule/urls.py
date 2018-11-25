from django.conf.urls  import include,url

from . import views

app_name = "elite_schedule"

urlpatterns = [
    url('upload', views.index, name='index'),
    url('matches',views.MatchListAPIView.as_view(), name='matches')
]