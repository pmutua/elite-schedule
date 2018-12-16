from django.views.generic import ListView
from .models import Match


class MatchList(ListView):
    model = Match
    
class EnglishPremierLeagueMatchList(ListView):
    queryset= (Match.objects.eng_premier_league())