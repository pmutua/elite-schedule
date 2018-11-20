import csv 

csv_file = csv.reader(open('E1.csv'))

next(csv_file)

"""
Add counters counters for how many games ended up in home dogs winning, and also how many did not.
"""
upsets = 0
non_upsets = 0 

"""
Since we want to see how betting on these events would do in real life, we also need to set up some variables about our bankroll and bet sizing.
"""

starting_bankroll = 100 
wagering_size = 5

bankroll = starting_bankroll 

"""Iterate over all games"""

for game in csv_file:
    home_team = game[2]
    away_team = game[3]

    home_goals = int(game[4])
    away_goals = int(game[5])

    home_odds = float(game[23])
    draw_odds = float(game[24])
    away_odds = float(game[25])

    if home_odds > away_odds:
        if home_goals > away_goals:
            upsets +=1
            bankroll += wagering_size * (home_odds-1)
        else:
            non_upsets += 1
            bankroll -= wagering_size 