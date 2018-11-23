from django.db import models

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

class Match(models.Model):
    div= models.CharField(max_length=20)
    date=models.CharField(max_length=20)
    home_team=models.CharField(max_length=20)
    away_team=models.CharField(max_length=20)