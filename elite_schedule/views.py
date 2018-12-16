from djnago.views.generic import ListView
from .models import Match


class MatchList(ListView):
    model = Match