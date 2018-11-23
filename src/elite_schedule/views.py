from django.shortcuts import render
import csv

def index(request):
    if "GET" == request.method:
        return render(request, 'elite_schedule/index.html', {})
    else:
        csv_file = request.FILES["csv_file"]

        # you may put validations here to check extension or file size
        csv_file = csv.reader(open('E1.csv'))
        next(csv_file)

        csv_data = list()
        for game in csv_file:
            row_data = list()
            home_team = game[2]
            away_team = game[3]

            home_goals = int(game[4])
            away_goals = int(game[5])

            home_odds = float(game[23])
            draw_odds = float(game[24])
            away_odds = float(game[25])

            csv_data.append(row_data)

        return render(request, 'elite_schedule/index.html', {"csv_data":csv_data})
