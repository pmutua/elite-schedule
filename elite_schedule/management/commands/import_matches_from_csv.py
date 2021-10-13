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
import re
import datetime
from django.core.management.base import BaseCommand
from elite_schedule.models import *
from  elite_schedule.utilities import remove_whitespaces
from .divisions import DIVISIONS,EXPECTED_COLUMNS
from collections import deque
from django.db.models import Q

SILENT, NORMAL, VERBOSE, VERY_VERBOSE = 0, 1, 2, 3

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# csv_files = ['bundesliga_1.csv','bundesliga_2.csv','eng_championship.csv','eng_conference.csv','eng_league_1.csv','eng_league_2.csv','eng_premier_league.csv','la_liga_primiera_division.csv','la_liga_segunda_division.csv','seria_a.csv','seria_b.csv']
csv_files = [
    'B1.csv',
    'D1.csv',
    'D2.csv',
    'E0.csv',
    'E1.csv',
    'E2.csv',
    'E3.csv',
    'EC.csv',
    'F1.csv',
    'F2.csv',
    'G1.csv',
    'I1.csv',
    'I2.csv',
    'N1.csv',
    'P1.csv',
    'SC0.csv',
    'SC1.csv',
    'SC2.csv',
    'SC3.csv',
    'SP1.csv',
    'SP2.csv',
    'T1.csv'

]

CSV_FOLDER_PATH = os.path.join(BASE_DIR, "data")

class Command(BaseCommand):
    help = ("Imports movies from a local CSV file. " "Expects title, URL, and release year.")
    
    # def add_arguments(self, parser):
    #     # Positional arguments
    #     parser.add_argument("file_path",nargs=1,type=str,)
    
    
    def handle(self, *args, **options):
        verbosity = options.get("verbosity", NORMAL)


#         Entry.objects.bulk_create([
#     Entry(headline="Django 1.0 Released"),
#     Entry(headline="Django 1.1 Announced"),
#     Entry(headline="Breaking: Django is awesome")
# ])
        # Initializing a queue
        match_objects = deque()
        for csv_file in csv_files:

            file_path = os.path.join(CSV_FOLDER_PATH,str(csv_file))
            print(file_path)
            if verbosity >= NORMAL:
                self.stdout.write("=== Matches imported ===")
            with open(file_path) as f:
                # reading the csv file using DictReader

                csv_reader = csv.reader(f, delimiter = ',')
            
                # list to store the names of columns
                list_of_column_names = []
            
                # loop to iterate through the rows of csv
                list_of_column_names = None
                for row in csv_reader:
            
                    # adding the first row
                    list_of_column_names = row

                    break
                # print(len(list_of_column_names))
                # TODO validated column or raise exception


                reader = csv.reader(f)
                # Dont upload header froom csv 
                next(reader)
                # TODO write a function Validate data is clean first
                # clean check wjite space white space


                
            
                for game in reader:
                    # if not in the list give it a default value
                    div = game[list_of_column_names.index('Div')] 
                    dt = game[list_of_column_names.index('Date')] 
                    time = game[list_of_column_names.index('Time')] 
                    ht = game[list_of_column_names.index('HomeTeam')] 
                    at = game[list_of_column_names.index('AwayTeam')] 
                    fthg = game[list_of_column_names.index('FTHG')] 
                    ftag = game[list_of_column_names.index('FTAG')] 
                    ftr = game[list_of_column_names.index('FTR')] 
                    hthg =  game[list_of_column_names.index('HTHG')] 
                    htag = game[list_of_column_names.index('HTAG')]
                    htr = game[list_of_column_names.index('HTR')]
                    HS = game[list_of_column_names.index('HS')]
                    AS = game[list_of_column_names.index('AS')]
                    HST= game[list_of_column_names.index('HST')]
                    AST = game[list_of_column_names.index('AST')]
                    HF = game[list_of_column_names.index('HF')]
                    HC = game[list_of_column_names.index('HC')]
                    AC = game[list_of_column_names.index('AC')]
                    HY = game[list_of_column_names.index('HY')]
                    AY = game[list_of_column_names.index('AY')]
                    HR = game[list_of_column_names.index('HR')]
                    AR = game[list_of_column_names.index('AR')]
                    B365H = game[list_of_column_names.index('B365H')]
                    B365D = game[list_of_column_names.index('B365D')]
                    B365A = game[list_of_column_names.index('B365A')]
                    BWH = game[list_of_column_names.index('BWH')]
                    BWD = game[list_of_column_names.index('BWD')]
                    BWA = game[list_of_column_names.index('BWA')]
                    IWH = game[list_of_column_names.index('IWH')]
                    IWD = game[list_of_column_names.index('IWD')]
                    IWA = game[list_of_column_names.index('IWA')]
                    PSH = game[list_of_column_names.index('PSH')]
                    PSD	= game[list_of_column_names.index('PSD')]
                    PSA	= game[list_of_column_names.index('PSA')]
                    WHH	= game[list_of_column_names.index('WHH')]
                    WHD	= game[list_of_column_names.index('WHD')]
                    WHA	= game[list_of_column_names.index('WHA')]
                    VCH	= game[list_of_column_names.index('VCH')]
                    VCD = game[list_of_column_names.index('VCD')]
                    VCA	= game[list_of_column_names.index('VCA')]
                    MaxH = game[list_of_column_names.index('MaxH')]
                    MaxD = game[list_of_column_names.index('MaxD')]
                    MaxA = game[list_of_column_names.index('MaxA')]
                    AvgH = game[list_of_column_names.index('AvgH')]
                    AvgD = game[list_of_column_names.index('AvgD')]
                    AvgA = game[list_of_column_names.index('AvgA')]
                    B365over2_5	= game[list_of_column_names.index('B365>2.5')]
                    B365under2_5 = game[list_of_column_names.index('B365<2.5')]
                    Pover2_5 = game[list_of_column_names.index('P>2.5')]
                    Punder2_5  = game[list_of_column_names.index('P<2.5')]
                    Maxover2_5 = game[list_of_column_names.index('Max>2.5')]
                    Maxunder2_5 =  game[list_of_column_names.index('Max<2.5')]
                    Avgover2_5 = game[list_of_column_names.index('Avg>2.5')]
                    Avgunder2_5 = game[list_of_column_names.index('Avg<2.5')]
                    AHh = game[list_of_column_names.index('AHh')]
                    B365AHH = game[list_of_column_names.index('B365AHH')]
                    B365AHA = game[list_of_column_names.index('B365AHA')]
                    PAHH = game[list_of_column_names.index('PAHH')]
                    PAHA = game[list_of_column_names.index('PAHA')]
                    MaxAHH = game[list_of_column_names.index('MaxAHH')]
                    MaxAHA = game[list_of_column_names.index('MaxAHA')]
                    AvgAHH =  game[list_of_column_names.index('AvgAHH')]
                    AvgAHA = game[list_of_column_names.index('AvgAHA')]
                    B365CH = game[list_of_column_names.index('B365CH')]
                    B365CD = game[list_of_column_names.index('B365CD')]
                    B365CA = game[list_of_column_names.index('B365CA')]
                    BWCH = game[list_of_column_names.index('BWCH')]
                    BWCD = game[list_of_column_names.index('BWCD')]
                    BWCA = game[list_of_column_names.index('BWCA')]
                    IWCH = game[list_of_column_names.index('IWCH')]
                    IWCD = game[list_of_column_names.index('IWCD')]
                    IWCA = game[list_of_column_names.index('IWCA')]
                    PSCH = game[list_of_column_names.index('PSCH')]
                    PSCD = game[list_of_column_names.index('PSCD')]
                    PSCA = game[list_of_column_names.index('PSCA')]
                    WHCH = game[list_of_column_names.index('WHCH')]
                    WHCD = game[list_of_column_names.index('WHCD')]
                    WHCA = game[list_of_column_names.index('WHCA')]
                    VCCH = game[list_of_column_names.index('VCCH')]
                    VCCD = game[list_of_column_names.index('VCCD')]
                    VCCA = game[list_of_column_names.index('VCCA')]
                    MaxCH = game[list_of_column_names.index('MaxCH')]
                    MaxCD = game[list_of_column_names.index('MaxCD')]
                    MaxCA = game[list_of_column_names.index('MaxCA')]
                    AvgCH = game[list_of_column_names.index('AvgCH')]
                    AvgCD = game[list_of_column_names.index('AvgCD')]
                    AvgCA = game[list_of_column_names.index('AvgCA')]
                    B365Cover2_5 = game[list_of_column_names.index('B365C>2.5')]
                    B365Cunder2_5 = game[list_of_column_names.index('B365C<2.5')]
                    PCover2_5 = game[list_of_column_names.index('PC>2.5')]
                    PCunder2_5 = game[list_of_column_names.index('PC<2.5')]
                    MaxCover2_5 = game[list_of_column_names.index('MaxC>2.5')]
                    MaxCunder2_5 = game[list_of_column_names.index('MaxC<2.5')]
                    AvgCover2_5 = game[list_of_column_names.index('AvgC>2.5')]
                    AvgCunder2_5 = game[list_of_column_names.index('AvgC<2.5')]
                    AHCh = game[list_of_column_names.index('AHCh')]
                    B365CAHH = game[list_of_column_names.index('B365CAHH')]
                    B365CAHA = game[list_of_column_names.index('B365CAHA')]
                    PCAHH = game[list_of_column_names.index('PCAHH')]
                    PCAHA = game[list_of_column_names.index('PCAHA')]
                    MaxCAHH = game[list_of_column_names.index('MaxCAHH')]
                    MaxCAHA = game[list_of_column_names.index('MaxCAHA')]
                    AvgCAHH = game[list_of_column_names.index('AvgCAHH')]
                    AvgCAHA = game[list_of_column_names.index('AvgCAHA')]
                    date=datetime.datetime.strptime(dt,'%d/%m/%Y').strftime('%Y-%m-%d')
                    # print(game)
                        # let's skip the column captions
                    # continue
                    """Assign country based on division.
                    to get divisions code details check football.uk
                    """ 

                    # TODO check if there is duplicate
                    try:
                        division,_ = Division.objects.get_or_create(code=div)
                        home_team,_ = Team.objects.get_or_create(name=ht)
                        away_team,_ = Team.objects.get_or_create(name=at)
                        
                    
                        match = \
                        Match(
                            division= division,
                            date= date,
                            time = time,
                            home_team = home_team,
                            away_team = away_team,
                            fthg = fthg,
                            ftag = ftag,
                            ftr =  ftr,
                            hthg = hthg,
                            htag = htag,
                            htr =  htr,
                            HS = HS,
                            AS = AS,
                            HST=HST,
                            AST = AST,
                            HF = HF,
                            HC = HC,
                            AC = AC,
                            HY = HY,
                            AY =AY,
                            HR = HR,
                            AR = AR,
                            B365H = B365H,
                            B365D = B365D,
                            B365A = B365A,
                            BWH =  BWH,
                            BWD = BWD,
                            BWA = BWA,
                            IWH = IWH,
                            IWD = IWD,
                            IWA = IWA,
                            PSH = PSH,
                            PSD	= PSD,
                            PSA	= PSA,
                            WHH	= WHH,
                            WHD	= WHD,
                            WHA	= WHA,
                            VCH	= VCH,
                            VCD = VCD,
                            VCA	= VCA,
                            MaxH = MaxH,
                            MaxD = MaxD,
                            MaxA = MaxA,
                            AvgH = AvgH,
                            AvgD = AvgD,
                            AvgA = AvgA,
                            B365over2_5	= B365over2_5,
                            B365under2_5 = B365under2_5,
                            Pover2_5 = Pover2_5,
                            Punder2_5  = Punder2_5,
                            Maxover2_5 = Maxover2_5,
                            Maxunder2_5 = Maxunder2_5,
                            Avgover2_5 =  Avgover2_5,
                            Avgunder2_5 = Avgunder2_5,
                            AHh = AHh,
                            B365AHH = B365AHH,
                            B365AHA = B365AHA,
                            PAHH = PAHH,
                            PAHA = PAHA,
                            MaxAHH =  MaxAHH,
                            MaxAHA = MaxAHA,
                            AvgAHH = AvgAHH,
                            AvgAHA = AvgAHA,
                            B365CH = B365CH,
                            B365CD = B365CD,
                            B365CA =  B365CA,
                            BWCH = BWCH,
                            BWCD = BWCD,
                            BWCA = BWCA,
                            IWCH =  IWCH,
                            IWCD = IWCD,
                            IWCA = IWCA,
                            PSCH = PSCH,
                            PSCD = PSCD,
                            PSCA = PSCA,
                            WHCH = WHCH,
                            WHCD = WHCD,
                            WHCA = WHCA,
                            VCCH = VCCH,
                            VCCD = VCCD,
                            VCCA = VCCA,
                            MaxCH = MaxCH,
                            MaxCD = MaxCD,
                            MaxCA = MaxCA,
                            AvgCH = AvgCH,
                            AvgCD = AvgCD,
                            AvgCA = AvgCA,
                            B365Cover2_5 = B365Cover2_5,
                            B365Cunder2_5 = B365Cunder2_5,
                            PCover2_5 = PCover2_5,
                            PCunder2_5 = PCunder2_5,
                            MaxCover2_5 = MaxCover2_5,
                            MaxCunder2_5 = MaxCunder2_5,
                            AvgCover2_5 = AvgCover2_5,
                            AvgCunder2_5 = AvgCunder2_5,
                            AHCh =  AHCh,
                            B365CAHH = B365CAHH,
                            B365CAHA = B365CAHA,
                            PCAHH = PCAHH,
                            PCAHA = PCAHA,
                            MaxCAHH = MaxCAHH,
                            MaxCAHA = MaxCAHA,
                            AvgCAHH = AvgCAHH,
                            AvgCAHA = AvgCAHA 
                        )

                        match_objects.append(match)
                        
                        if verbosity >= NORMAL:
                            pass
                            # self.stdout.write(f"{ht} vs {at}")
                    except Exception as e:
                        # what to do when this error happens send logs 
                        raise e

        match_object_list = list(match_objects)
        count_match_object_list = len(match_object_list)
        self.stdout.write(f"{count_match_object_list} record(s) found bulk inserting into database...") 

        created_objects = Match.objects.bulk_create(match_object_list,ignore_conflicts=True)

        count_created_objects =len(created_objects)

        self.stdout.write(f"{count_created_objects} record(s) inserted into database...") 
        # print(match_objects.count())
        
