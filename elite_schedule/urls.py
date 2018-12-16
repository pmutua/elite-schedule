from django.urls import path 

from . import views 


app_name = 'elite_schedule'

urlpatterns = [
    path('matches', views.MatchList.as_view(),name='MatchList'),
    path('english_premier_league', views.EnglishPremierLeagueMatchList.as_view(),name='EnglishPremierLeague')
]