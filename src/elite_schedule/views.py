import csv

import os

from django.shortcuts import render, get_object_or_404
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

from django.http import Http404
from django.db.models import Q
from rest_framework.filters import (
    SearchFilter
)

from django.shortcuts import render
from rest_framework import generics

from .models import (Match,)
from elite_schedule import serializers as ser
from .serializers import (MatchSerializer,)

import json 

class MatchHistoryViewset(viewsets.ViewSet):
    """
    API: /matches/
    Method: GET

    A class based view that provides the standard actions `GET`.

    """
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    def list(self, request):
        """List all matches."""
        queryset = Match.objects.all()
        serializer = MatchSerializer(queryset, many=True)
        return Response(serializer.data)

class TeamSearchAPIView(generics.ListAPIView):
    """ Class based view for team search api view. """
    serializer_class = MatchSerializer
    queryset = Match.objects.none()

    def get_queryset(self, *args, **kwargs):
        """This wil list all games a team has played either home or way.
        This queries a team based on name parameters.
            for example  `team/search/?=swansea`
        
        """        
        queryset_list = Match.objects.filter(
            id__gte=0)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(home_team__icontains=query)|
                Q(away_team__icontains=query)
            ).distinct()
        serializer =MatchSerializer(queryset_list, many=True)
        
        return queryset_list

class EnglandMatchesViewSet(viewsets.ViewSet):
    """
    A viewset that provides the standard actions POST,GET,DELETE,PUT.
    """
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    def list(self, request):
        """List all matches played from English Leagues."""
        queryset = Match.objects.filter(
                Q(division__icontains="E0")|
                Q(division__icontains="E1")|
                Q(division__icontains="E2")|
                Q(division__icontains="EC")
                )
        serializer = MatchSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def premier_leage(self, request):
        """Lists down all ."""
        matches = Match.objects.eng_premier_league()
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def conference(self, request):
        """Lists down all English Conference matches."""
        matches = Match.objects.eng_conference()
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def league_1(self, request):
        """Lists down all English League 1 matches."""
        matches = Match.objects.eng_league_1()
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def league_2(self, request):
        """Lists down all English League 2 matches."""
        matches = Match.objects.eng_league_2()
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)

class SpainMatchesViewSet(viewsets.ViewSet):
    """
    A viewset that provides the standard action `GET`.
    """
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    def list(self, request):
        """List all matches from Spanish Leagues."""
        queryset = Match.objects.filter(
                Q(division__icontains="SP1")|
                Q(division__icontains="SP2")
                )
        serializer = MatchSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def laliga_primiera(self, request):
        """Lists down all La Liga primiera matches."""
        matches = Match.objects.la_liga_primiera()
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def la_liga_segunda(self, request):
        """Lists down all La SLiga Segunda matches."""
        matches = Match.objects.accepted()
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)


class GermanyMatchesViewSet(viewsets.ViewSet):
    """
    A viewset that provides one standard action `GET`.
    """
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    def list(self, request):
        """List all matches from German Leagues."""
        queryset = Match.objects.filter(
                Q(division__icontains="D1")|
                Q(division__icontains="D2")
                )
        serializer = MatchSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def bundesliga_1(self, request):
        """Lists down all Bundesliga 1 matches."""
        matches = Match.objects.bundesliga_1()
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def bundesliga_2(self, request):
        """Lists down all Bundesliga 2 matches."""
        matches = Match.objects.bundesliga_2()
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)

class ItalyMatchesViewSet(viewsets.ViewSet):
    """
    A viewset that provides one standard action `GET`.
    """
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    def list(self, request):
        """List all matches from Italian Leagues."""
        queryset = Match.objects.filter(
                Q(division__icontains="I1")|
                Q(division__icontains="I2")
                )
        serializer = MatchSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def seria_a(self, request):
        """Lists down all Seria A matches."""
        matches = Match.objects.seria_a()
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def seria_b(self, request):
        """Lists down all Seria B matches."""
        matches = Match.objects.seria_b()
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)



