from django.contrib import admin
from elite_schedule.models import *


admin.site.register(Division)


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = (
        'division',
        'date',
        'time',
        'home_team',
        'away_team',
        'fthg',
        'ftag',
        'ftr',
        'hthg',
        'htag',
        'htr',
        'HS',
        'AvgCAHA'

    )
    search_fields = (
        'division__code',
        'home_team__name',
        'away_team__name',

    )
