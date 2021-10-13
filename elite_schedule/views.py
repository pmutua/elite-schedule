from django.views.generic import ListView,DetailView
from django.shortcuts import render

from .models import Match
import operator

from django.db.models import Q




def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Match.objects.all().count()
    # num_instances = Match.all().count()
    
    # Available books (status = 'a')
    # num_instances_available = Match.filter(status__exact='a').count()
    
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
    queryset = Match.objects.all()



class TeamSearchListView(MatchList):
    """
    Display a Team objects List page filtered by the search query.
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
    queryset= Match.english_premier_league.all()

class EnglishConferenceMatchList(ListView):
    queryset= Match.english_conference.all()

class EnglishLeagueOneMatchList(ListView):
    queryset= Match.english_league_1.all()

class EnglishLeagueTwoMatchList(ListView):
    queryset= Match.english_league_2.all()

class BundesligaLeagueOneMatchList(ListView):
    queryset= Match.bundesliga_1.all()

class BundesligaLeagueTwoMatchList(ListView):
    queryset= Match.bundesliga_2.all()

class LaligaPrimieraMatchList(ListView):
    queryset= Match.laliga_primiera.all()

class LaligaSegundaMatchList(ListView):
    queryset= Match.laliga_segunda.all()

class Serie_A_MatchList(ListView):
    queryset= Match.serie_a.all()

class Serie_B_MatchList(ListView):
    queryset= Match.serie_b.all()

class Jackpots(ListView):
    pass
    
class SportPesaJackpot(ListView):
    pass 

class BetPawaJackpot(ListView):
    pass