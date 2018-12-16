from django.views.generic import ListView,DetailView

from .models import Match


class MatchList(ListView):
    model = Match
    
class MatchDetail(DetailView):
    model = Match

class EnglishPremierLeagueMatchList(ListView):
    queryset= (Match.objects.eng_premier_league())

class EnglishConferenceMatchList(ListView):
    queryset= (Match.objects.eng_conference())

class EnglishLeagueOneMatchList(ListView):
    queryset= (Match.objects.eng_league_1())

class EnglishLeagueTwoMatchList(ListView):
    queryset= (Match.objects.eng_league_2())

class BundesligaLeagueOneMatchList(ListView):
    queryset= (Match.objects.bundesliga_1())

class BundesligaLeagueTwoMatchList(ListView):
    queryset= (Match.objects.bundesliga_2())

class LaLigaPrimieraMatchList(ListView):
    queryset= (Match.objects.la_liga_primiera())

class LaligaSegundaMatchList(ListView):
    queryset= (Match.objects.la_liga_segunda())

class LaligaPrimieraMatchList(ListView):
    queryset= (Match.objects.la_liga_primiera())

class Serie_A_MatchList(ListView):
    queryset= (Match.objects.serie_a())

class Serie_B_MatchList(ListView):
    queryset= (Match.objects.serie_b())

class Jackpots(ListView):
    pass
    
class SportPesaJackpot(ListView):
    pass 

class BetPawaJackpot(ListView):
    pass