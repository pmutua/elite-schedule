from django.views.generic import ListView
from .models import Match


class MatchList(ListView):
    model = Match
    
class EnglishPremierLeagueMatchList(ListView):
    queryset= (Match.objects.eng_premier_league())

class EnglishConferenceMatchList(ListView):
    queryset= (Match.objects.eng_conference())

class EnglishLeagueOneMatchList(ListView):
    queryset= (Match.objects.eng_league_1())

class EnglishLeagueTwoMatchList(ListView):
    queryset= (Match.objects.eng_league_2())