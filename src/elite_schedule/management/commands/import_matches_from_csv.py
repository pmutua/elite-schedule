# -*- coding: UTF-8 -*-
"""
    Author: Philip Mutua 
    Github: @pmutua
"""
from __future__ import unicode_literals
import csv
from django.core.management.base import BaseCommand
from elite_schedule.models import Match
SILENT, NORMAL, VERBOSE, VERY_VERBOSE = 0, 1, 2, 3

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

x=os.path.join(BASE_DIR, 'matches.csv')



class Command(BaseCommand):
    help = ("Imports movies from a local CSV file. " "Expects title, URL, and release year.")
    
    # def add_arguments(self, parser):
    #     # Positional arguments
    #     parser.add_argument("file_path",nargs=1,type=str,)
    
    
    def handle(self, *args, **options):
        verbosity = options.get("verbosity", NORMAL)
        file_path = x
        print(file_path)
        if verbosity >= NORMAL:
            self.stdout.write("=== Matches imported ===")
        with open(file_path) as f:
            reader = csv.reader(f)
            # Dont upload header froom csv 
            next(reader)
            for game in reader:
                division = game[0]
                date=game[1]
                home_team = game[2]
                away_team = game[3]

                home_goal = game[4]
                away_goal = game[5]
                print(home_goal)
                home_odd = game[23]
                draw_odd = game[24]
                away_odd = game[25]
                    # let's skip the column captions
                # continue
                if division == "E1":
                    country = "ENGLAND"
                    match, created = \
                    Match.objects.get_or_create(
                    division=division,
                    date=date,
                    home_team=home_team,
                    away_team=away_team,
                    home_goal =home_goal,
                    away_goal=away_goal,
                    home_odd=home_odd,
                    draw_odd=draw_odd,
                    away_odd=away_odd,
                    country=country
                    )
                    if verbosity >= NORMAL:
                        self.stdout.write("{}. {}".format(game, match.division))