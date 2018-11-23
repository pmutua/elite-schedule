import csv

csv_file = csv.reader(open('E1.csv'))
next(csv_file)


home = []
away = []

for game in csv_file:
    home_team = game[2]
    away_team = game[3]

    home_goals = int(game[4])
    away_goals = int(game[5])

    home_odds = float(game[23])
    draw_odds = float(game[24])
    away_odds = float(game[25])

    home.append(home_team)
    away.append(away_team)
    print(game)