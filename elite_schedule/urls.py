from django.urls import path 

from . import views 


app_name = 'elite_schedule'

urlpatterns = [
    path('matches', views.MatchList.as_view(),name='MatchList')
]