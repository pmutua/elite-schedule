from django.views.generic import ListView,DetailView
from django.shortcuts import render

from .models import Match
import operator

from django.db.models import Q




def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Match.objects.all().count()
    # num_instances = Match.objects.all().count()
    
    # Available books (status = 'a')
    # num_instances_available = Match.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    # num_authors = Author.objects.count()
    
    context = {
        'num_books': num_books,
        # 'num_instances': num_instances,
        # 'num_instances_available': num_instances_available,
        # 'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'elite_schedule/index.html', context=context)



class MatchList(ListView):
    model = Match


class TeamSearchListView(MatchList):
    """
    Display a Team matches List page filtered by the search query.
    """
    paginate_by = 10

    def get_queryset(self):
        result = super(TeamSearchListView, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(title__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(content__icontains=q) for q in query_list))
            )

        return result
    
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