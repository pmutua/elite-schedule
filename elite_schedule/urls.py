from django.urls import path 

from . import views 


app_name = 'elite_schedule'

urlpatterns = [
    path('matches', views.MatchList.as_view(),name='MatchList'),
    path('english_premier_league', views.EnglishPremierLeagueMatchList.as_view(),name='EnglishPremierLeague'),
    path('english_conference', views.EnglishConferenceMatchList.as_view(),name='EnglishConference'),
    path('english_league_1', views.EnglishLeagueOneMatchList.as_view(),name='EnglishLeagueOne'),
    path('english_league_2', views.EnglishLeagueTwoMatchList.as_view(),name='EnglishLeagueTwo')
]