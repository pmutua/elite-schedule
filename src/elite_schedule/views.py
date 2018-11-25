import csv

import os

from django.shortcuts import render
from rest_framework import generics

from .models import (Match,)
from .serializers import (MatchSerializer,)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def index(request):
    csv_file = csv.reader(open(os.path.join(BASE_DIR, 'E1.csv')))
    next(csv_file)


    # iterating over the r
    home_tm= []
    away_tm = []
    
    home_gl=[]
    away_gl=[]
    
    home_od =[]
    draw_od = []
    away_od = [] 


    data = {
        "home":home_tm,
        "away_tm":away_tm
    }

    for game in csv_file:
        home_team = game[2]
        away_team = game[3]

        home_goals = int(game[4])
        away_goals = int(game[5])

        home_odds = float(game[23])
        draw_odds = float(game[24])
        away_odds = float(game[25])
        
        home_tm.append(home_team)
        away_tm.append(home_team)

        home_gl.append(home_goals)
        away_gl.append(away_goals)

        home_od = home_odds
        draw_od = draw_odds
        away_od = away_odds 

        # csv_data.append(row_data)

    return render(request, 'elite_schedule/index.html', {"csv_data":data})


class MatchListAPIView(generics.ListAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer