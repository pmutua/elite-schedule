from django.urls import path 

from . import views 


app_name = 'elite_schedule'

urlpatterns = [
    path('matches', views.MatchList.as_view(),name='MatchList'),
    path('english_premier_league', views.EnglishPremierLeagueMatchList.as_view(),name='EnglishPremierLeague'),
    path('english_conference', views.EnglishConferenceMatchList.as_view(),name='EnglishConference'),
    path('english_league_1', views.EnglishLeagueOneMatchList.as_view(),name='EnglishLeagueOne'),
    path('english_league_2', views.EnglishLeagueTwoMatchList.as_view(),name='EnglishLeagueTwo'),
    path('bundesliga_1', views.BundesligaLeagueOneMatchList.as_view(),name='BundesligaLeagueOne'),
    path('bundesliga_2', views.BundesligaLeagueTwoMatchList.as_view(),name='BundesligaLeagueTwo'),
    path('laliga_primiera', views.LaligaPrimieraMatchList.as_view(),name='LaligaPrimiera'),
    path('laliga_segunda', views.LaligaSegundaMatchList.as_view(),name='LaligaSegunda'),
    path('serie_a', views.Serie_A_MatchList.as_view(),name='SerieA'),
    path('serie_b', views.Serie_B_MatchList.as_view(),name='SerieB'),

]
