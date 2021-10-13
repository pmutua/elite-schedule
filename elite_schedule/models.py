# System libraries
# from datetime import datetime
# # Third-party libraries
# Django modules

from uuid import uuid4
from django.conf import settings 
from django.db import models
# # Django apps if any 
# # Current-app modules
from .managers import *


def team_directory_path_with_uuid(
    instance, filename):
    return '{}/{}'.format(instance.team_id,uuid4())

class Division(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    flag = models.ImageField(blank=True,null=True)

    def __str__(self):
        return self.code

class Team(models.Model):
    name = models.CharField(max_length=90)
    logo = models.ImageField(upload_to=team_directory_path_with_uuid,blank=True,null=True)
    division = models.ForeignKey(Division,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.name


class Match(models.Model):
    division= models.ForeignKey(Division,on_delete=models.CASCADE)
    date= models.DateField()
    time = models.TimeField(blank=True,null=True)
    home_team = models.ForeignKey('Team', related_name='home_team',on_delete=models.CASCADE)
    away_team = models.ForeignKey('Team', related_name='away_team',on_delete=models.CASCADE)
    fthg = models.CharField(max_length=20)
    ftag = models.CharField(max_length=20)
    ftr = models.CharField(max_length=20)
    hthg = models.CharField(max_length=20)
    htag = models.CharField(max_length=20)
    htr = models.CharField(max_length=20)
    HS = models.CharField(max_length=20)
    AS = models.CharField(max_length=20)
    HST= models.CharField(max_length=20)
    AST = models.CharField(max_length=20)
    HF = models.CharField(max_length=20)
    HC = models.CharField(max_length=20)
    AC = models.CharField(max_length=20)
    HY = models.CharField(max_length=20)
    AY = models.CharField(max_length=20)
    HR = models.CharField(max_length=20)
    AR = models.CharField(max_length=20)
    B365H = models.CharField(max_length=20)
    B365D = models.CharField(max_length=20)
    B365A = models.CharField(max_length=20)
    BWH = models.CharField(max_length=20)
    BWD = models.CharField(max_length=20)
    BWA = models.CharField(max_length=20)
    IWH = models.CharField(max_length=20)
    IWD = models.CharField(max_length=20)
    IWA = models.CharField(max_length=20)
    PSH = models.CharField(max_length=20)
    PSD	= models.CharField(max_length=20)
    PSA	= models.CharField(max_length=20)
    WHH	= models.CharField(max_length=20)
    WHD	= models.CharField(max_length=20)
    WHA	= models.CharField(max_length=20)
    VCH	= models.CharField(max_length=20)
    VCD = models.CharField(max_length=20)
    VCA	= models.CharField(max_length=20)
    MaxH = models.CharField(max_length=20)
    MaxD = models.CharField(max_length=20)
    MaxA = models.CharField(max_length=20)
    AvgH = models.CharField(max_length=20)
    AvgD = models.CharField(max_length=20)
    AvgA = models.CharField(max_length=20)
    B365over2_5	= models.CharField(max_length=20)
    B365under2_5 = models.CharField(max_length=20)	
    Pover2_5 = models.CharField(max_length=20)
    Punder2_5  = models.CharField(max_length=20)
    Maxover2_5 = models.CharField(max_length=20)
    Maxunder2_5 =  models.CharField(max_length=20)
    Avgover2_5 = models.CharField(max_length=20)
    Avgunder2_5 = models.CharField(max_length=20)
    AHh = models.CharField(max_length=20)
    B365AHH = models.CharField(max_length=20)
    B365AHA = models.CharField(max_length=20)
    PAHH = models.CharField(max_length=20)
    PAHA = models.CharField(max_length=20)
    MaxAHH = models.CharField(max_length=20)
    MaxAHA = models.CharField(max_length=20)
    AvgAHH = models.CharField(max_length=20)
    AvgAHA = models.CharField(max_length=20)
    B365CH = models.CharField(max_length=20)
    B365CD = models.CharField(max_length=20)
    B365CA = models.CharField(max_length=20)
    BWCH = models.CharField(max_length=20)
    BWCD = models.CharField(max_length=20)
    BWCA = models.CharField(max_length=20)
    IWCH = models.CharField(max_length=20)
    IWCD = models.CharField(max_length=20)
    IWCA = models.CharField(max_length=20)
    PSCH = models.CharField(max_length=20)
    PSCD = models.CharField(max_length=20)
    PSCA = models.CharField(max_length=20)
    WHCH = models.CharField(max_length=20)
    WHCD = models.CharField(max_length=20)
    WHCA = models.CharField(max_length=20)
    VCCH = models.CharField(max_length=20)
    VCCD = models.CharField(max_length=20)
    VCCA = models.CharField(max_length=20)
    MaxCH = models.CharField(max_length=20)
    MaxCD = models.CharField(max_length=20)
    MaxCA = models.CharField(max_length=20)
    AvgCH = models.CharField(max_length=20)
    AvgCD = models.CharField(max_length=20)
    AvgCA = models.CharField(max_length=20)
    B365Cover2_5 = models.CharField(max_length=20)
    B365Cunder2_5 = models.CharField(max_length=20)
    PCover2_5 = models.CharField(max_length=20)
    PCunder2_5 = models.CharField(max_length=20)
    MaxCover2_5 = models.CharField(max_length=20)
    MaxCunder2_5 = models.CharField(max_length=20)
    AvgCover2_5 = models.CharField(max_length=20)
    AvgCunder2_5 = models.CharField(max_length=20)
    AHCh = models.CharField(max_length=20)
    B365CAHH = models.CharField(max_length=20)
    B365CAHA = models.CharField(max_length=20)
    PCAHH = models.CharField(max_length=20)
    PCAHA = models.CharField(max_length=20)
    MaxCAHH = models.CharField(max_length=20)
    MaxCAHA = models.CharField(max_length=20)
    AvgCAHH = models.CharField(max_length=20)
    AvgCAHA = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    

    objects = models.Manager()
    english_premier_league = EnglishPremierLeagueManager()
    english_conference =  EnglishConference()
    english_league_1 = EnglishLeague1()
    english_league_2 = EnglishLeague2Manager()
    bundesliga_1 = Bundesliga1Manager()
    bundesliga_2 = Bundesliga2Manger()
    laliga_primiera = LaligaPrimieraManager()
    laliga_segunda = LaligaSegundaManager()
    serie_a = SerieAManager()
    serie_b = SerieBManager()
    england_matches = EnglandMatchesManager()
    german_matches = GermanMatchesManager()
    spanish_matches = SpanishMatchesManager()
    italian_matches = ItalianMatchesManager()

    """
    This example allows you to request Person.authors.all(), Person.editors.all(), and Person.people.all(), yielding predictable results.
    """

    class Meta:
        db_table = 'match'
        managed = True
        verbose_name = 'Match'
        verbose_name_plural = 'Matches'

    def __str__(self):
        return f'{self.home_team.name}--{self.time}--{self.away_team.name}'


    

