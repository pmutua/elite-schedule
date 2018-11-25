from django.db import models
from utils import CountryChoice 
# Create your models here.

# -*- coding: UTF-8 -*-
# System libraries
# from __future__ import unicode_literals
# import os
# import re
# from datetime import datetime
# # Third-party libraries
# import boto
# from PIL import Image
# # Django modules
# from django.db import models
# from django.conf import settings
# # Django apps
# from cms.models import Page
# # Current-app modules
# from . import app_settings



class MatchManager(models.Manager):
    # Add query by divisions ie EPL,Laliga etc
    def e_1_division(self):
        return self.filter(division='E1')
    def accepted(self):
        return  self.filter(bid_status='ACCEPTED')

# TODO division choices 


class Match(models.Model):
    EN = 1
    SP = 2
    IT = 3
    
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