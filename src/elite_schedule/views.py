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
from elite_schedule.base_generic_view import BaseRetrieveUpdateDestroyView
from django.shortcuts import render
from rest_framework import generics

from .models import (Match,)
from elite_schedule import serializers as ser
from .serializers import (MatchSerializer,)
from .serializer_utility import MethodSerializerView
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

class EnglandViewSet(viewsets.ViewSet, MethodSerializerView):
    """
    A viewset that provides the standard actions POST,GET,DELETE,PUT.
    """
    queryset = Match.objects.all()
    method_serializer_classes = {
        ('GET'): ser.MatchSerializer,
       
    }

    def list(self, request):
        """List all matches played from English Leagues."""
        queryset = Match.objects.all()
        serializer = MatchSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def league_1(self, request):
        """Lists down all ."""
        matches = Match.objects.awaiting()
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def league_2(self, request):
        """Lists down all."""
        matches = Match.objects.accepted()
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)

class SpainViewSet(viewsets.ViewSet, MethodSerializerView):
    """
    A viewset that provides the standard action `GET`.
    """
    queryset = Match.objects.all()
    method_serializer_classes = {
        ('GET',): ser.MatchSerializer,
       
    }
    def list(self, request):
        """List all matches from Spanish Leagues."""
        queryset = Match.objects.all()
        serializer = MatchSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def league_1(self, request):
        """Lists down all ."""
        matches = Match.objects.awaiting()
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def league_2(self, request):
        """Lists down all."""
        matches = Match.objects.accepted()
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)


class ItalyViewSet(viewsets.ViewSet, MethodSerializerView):
    """
    A viewset that provides one standard action `GET`.
    """
    queryset = Match.objects.all()
    method_serializer_classes = {
        ('GET'): ser.MatchSerializer,
       
    }

    def list(self, request):
        """List all matches from Italian Leagues."""
        queryset = Match.objects.all()
        serializer = MatchSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def league_1(self, request):
        """Lists down all ."""
        matches = Match.objects.awaiting()
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def league_2(self, request):
        """Lists down all."""
        matches = Match.objects.accepted()
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)



class GermanyViewSet(viewsets.ViewSet, MethodSerializerView):
    """
    A viewset that provides one standard action `GET`.
    """
    queryset = Match.objects.all()
    method_serializer_classes = {
        ('GET'): ser.MatchSerializer,
       
    }

    def list(self, request):
        """List all matches from German Leagues."""
        queryset = Match.objects.all()
        serializer = MatchSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def league_1(self, request):
        """Lists down all ."""
        matches = Match.objects.awaiting()
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def league_2(self, request):
        """Lists down all."""
        matches = Match.objects.accepted()
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)