
from django.db import models


class MatchManager(models.Manager):
    """Manager to query matches by divisions, i.e EPL, Laliga, Bundesliga, etc
    """
    def eng_premier_league(self):
        return self.filter(division='E0')
    
    def eng_conference(self):
        return  self.filter(division='EC')
    
    def eng_league_1(self):
        return  self.filter(division='E1')

    def eng_league_2(self):
        return self.filter(division='E2')

    def bundesliga_1(self):
        return self.filter(division='D1')
    
    def bundesliga_2(self):
        return  self.filter(division='D2')
    
    def la_liga_primiera(self):
        return  self.filter(division='S1')
    
    def la_liga_segunda(self):
        return  self.filter(division='S2')
      
    def serie_a(self):
        return  self.filter(division='I1')
    
    def serie_b(self):
        return self.filter(division='I2')
 