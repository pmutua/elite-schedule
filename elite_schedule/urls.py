from django.conf.urls import url

from . import views 


app_name = 'elite_schedule'

urlpatterns = [
    url('',views.index, name='index'),
    url('matches', views.MatchList.as_view(),name='MatchList'),
    url('english_premier_league', views.EnglishPremierLeagueMatchList.as_view(),name='EnglishPremierLeague'),
    url('english_conference', views.EnglishConferenceMatchList.as_view(),name='EnglishConference'),
    url('english_league_1', views.EnglishLeagueOneMatchList.as_view(),name='EnglishLeagueOne'),
    url('english_league_2', views.EnglishLeagueTwoMatchList.as_view(),name='EnglishLeagueTwo'),
    url('bundesliga_1', views.BundesligaLeagueOneMatchList.as_view(),name='BundesligaLeagueOne'),
    url('bundesliga_2', views.BundesligaLeagueTwoMatchList.as_view(),name='BundesligaLeagueTwo'),
    url('laliga_primiera', views.LaligaPrimieraMatchList.as_view(),name='LaligaPrimiera'),
    url('laliga_segunda', views.LaligaSegundaMatchList.as_view(),name='LaligaSegunda'),
    url('serie_a', views.Serie_A_MatchList.as_view(),name='SerieA'),
    url('serie_b', views.Serie_B_MatchList.as_view(),name='SerieB'),

    url('match/<int:pk>', views.MatchDetail.as_view(),name='MatchDetail')

]
