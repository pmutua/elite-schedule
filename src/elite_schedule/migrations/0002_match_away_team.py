# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-23 21:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elite_schedule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='away_team',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
