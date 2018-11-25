# System libraries
# from datetime import datetime
# # Third-party libraries
# Django modules
from django.db import models
# # Django apps if any 
# # Current-app modules
from .managers import MatchManager

class Match(models.Model):
    EN = 1
    SP = 2
    IT = 3
    GE = 4 
    
    COUNTRY_CHOICE = (
        (EN,"ENGLAND"),
        (SP,"SPAIN"),
        (IT,"ITALY"),
        (GE,"GERMANY"),
    )

    division= models.CharField(max_length=20)
    date=models.CharField(max_length=20)
    home_team=models.CharField(max_length=20)
    away_team=models.CharField(max_length=20)
    home_goal = models.CharField(max_length=20)
    away_goal = models.CharField(max_length=20)
    home_odd = models.CharField(max_length=20)
    draw_odd = models.CharField(max_length=20)
    away_odd = models.CharField(max_length=20)
    country = models.CharField(max_length=20,choices=COUNTRY_CHOICE)  # Choices is a list of Tuple)

    objects = MatchManager()