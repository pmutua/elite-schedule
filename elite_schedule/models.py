# System libraries
# from datetime import datetime
# # Third-party libraries
# Django modules

from uuid import uuid4
from django.conf import settings 
from django.db import models
# # Django apps if any 
# # Current-app modules
from .managers import MatchManager

class Match(models.Model):
    division= models.CharField(max_length=20)
    date=models.CharField(max_length=20)
    home_team=models.CharField(max_length=20)
    away_team=models.CharField(max_length=20)
    home_goal = models.CharField(max_length=20)
    away_goal = models.CharField(max_length=20)
    home_odd = models.CharField(max_length=20)
    draw_odd = models.CharField(max_length=20)
    away_odd = models.CharField(max_length=20)

    objects = MatchManager()

    class Meta:
        db_table = 'match'
        managed = True
        verbose_name = 'Match'
        verbose_name_plural = 'Matches'

    def __str__(self):
        return self.home_team

# def team_directory_path_with_uuid(
#     instance, filename):
#     return '{}/{}'.format(instance.team_id,uuid4())

# class TeamImage(models.Model):
#     image = models.ImageField(upload_to=team_directory_path_with_uuid)
#     uploaded= models.DateTimeField(auto_now_add=True)
#     Team= models.ForeignKey(Team,on_delete=models.CASCADE)
    

