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
        ('GET','PUT','PATCH', 'DELETE',): ser.MatchSerializer,
       
    }

    def list(self, request):
        """List all bids."""
        queryset = Match.objects.all()
        serializer = MatchSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def awaiting_bid_items(self, request):
        """Lists down all awaiting bid items."""
        awaiting_bid_items = Match.objects.awaiting()
        serializer = MatchSerializer(awaiting_bid_items, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def accepted_bid_items(self, request):
        """Lists down all accepted bid items."""
        accepted_bid_items = BidItem.objects.accepted()
        serializer = self.get_serializer(accepted_bid_items, many=True)
        return Response(serializer.data)



# TODO dd viewsets in coutries 