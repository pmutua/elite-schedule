#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
MIT License

Copyright (c) 2018 Philip Mutua, pmutua@live.com

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""
from __future__ import unicode_literals
import csv
from django.core.management.base import BaseCommand
from elite_schedule.models import Match
SILENT, NORMAL, VERBOSE, VERY_VERBOSE = 0, 1, 2, 3

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

csv_files = ['bundesliga_1.csv','bundesliga_2.csv','eng_championship.csv','eng_conference.csv','eng_league_1.csv','eng_league_2.csv','eng_premier_league.csv','la_liga_primiera_division.csv',' La_Liga_Segunda Division.csv','seria_a.csv','seria_b.csv']

CSV_FOLDER_PATH = os.path.join(BASE_DIR, "data")

class Command(BaseCommand):
    help = ("Imports movies from a local CSV file. " "Expects title, URL, and release year.")
    
    # def add_arguments(self, parser):
    #     # Positional arguments
    #     parser.add_argument("file_path",nargs=1,type=str,)
    
    
    def handle(self, *args, **options):
        verbosity = options.get("verbosity", NORMAL)
        for csv_file in csv_files:

            file_path = CSV_FILE_PATH = os.path.join(CSV_FOLDER_PATH,str(csv_file))
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
                    print(game)
                        # let's skip the column captions
                    # continue
                    """Assign country based on division.
                    to get divisions code details check football.uk
                    """ 
                    try: 
                             
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
                        away_odd=away_odd
                        )
                        if verbosity >= NORMAL:
                            self.stdout.write("{}. {}".format(game, match.division))
                    except Exception as e:
                        raise e 
        
