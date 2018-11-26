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
from .base_generic_view import BaseRetrieveUpdateDestroyView
from elite_schedule import serializers

from django.shortcuts import render
from rest_framework import generics

from .models import (Match,)
from elite_schedule import serializers as ser
from .serializers import (MatchSerializer,)

import json 

class MatchHistoryViewset(viewsets.ViewSet,generics.ListAPIView):
    """
        Show Matches
        
        ----
        Returns json data about a list of matches from all Leagues.
        =======================================

        * **URL**

            /matches/

        *  **URL Params**

            None

        * **Data Params**

            None
        
        * **Error Response:**

            * **Code:** 404 NOT FOUND <br />
            **Content:** `{ error : "Matches doesn't exist" }`

            OR

            * **Code:** 401 UNAUTHORIZED <br />
            **Content:** `{ error : "You are unauthorized to make this request." }`

        * **Sample Call:**

            ```bash
            curl -H "Authorization: JWT <your_token>" -H "Content-Type: application/json" http://localhost:8000/api/elite_schedule/matches/

            ```

    """
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    def get_queryset(self, request):
        queryset = Match.objects.all()
        serializer = MatchSerializer(queryset, many=True)
        return Response(serializer.data)

class TeamSearchAPIView(viewsets.ViewSet,generics.ListAPIView):
    """
        Search Team
        
        ----
        Returns json data about a single team,this will list all games a team has played both home or way. 

        * **URL**

        /elite_schedule/team/search/

        * **Method:**

            `GET`

        *  **URL Params**

            ?q=[string]

        * **Data Params**

            None

        * **Error Response:**

        * **Code:** 404 NOT FOUND <br />
            **Content:** `{ error : "Team doesn't exist" }`

            OR

        * **Code:** 401 UNAUTHORIZED <br />
            **Content:** `{ error : "You are unauthorized to make this request." }`

        * **Sample Call:**

            ```bash
            curl -H "Authorization: JWT <your_token>" -H "Content-Type: application/json" http://127.0.0.1:8000/api/elite_schedule/team/search/?q=swansea

            ```

    """    
    serializer_class = MatchSerializer
    queryset = Match.objects.none()

    def get_queryset(self, *args, **kwargs):
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

class EnglandMatchesViewSet(viewsets.ViewSet,generics.ListAPIView):
    """
        Show all English League matches.
        
        ----
        Returns json data about a list of matches from English League Matches.
        =======================================

        * **URL**

            /england/

        * **Method:**

            `GET`
            
        *  **URL Params**

            None

        * **Data Params**

            None

        * **Error Response:**

            * **Code:** 404 NOT FOUND <br />
            **Content:** `{ error : "Matches doesn't exist" }`

            OR

            * **Code:** 401 UNAUTHORIZED <br />
            **Content:** `{ error : "You are unauthorized to make this request." }`

        * **Sample Call:**

            ```bash
            curl -H "Authorization: JWT <your_token>" -H "Content-Type: application/json" http://localhost:8000/api/elite_schedule/england/england

            ```

    """

    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    def get_queryset(self, request):
        queryset = Match.objects.filter(
                Q(division__icontains="E0")|
                Q(division__icontains="E1")|
                Q(division__icontains="E2")|
                Q(division__icontains="EC")
                )
        serializer = MatchSerializer(queryset,many=True)
        return Response(data=serializer.data)

    @action(detail=False)
    def premier_leage(self, request):
        """
            Show all Premier League matches.
            
            ----
            Returns json data about a list of matches from English Premier League Matches.
            =======================================

            * **URL**

                /england/premier_leage

            * **Method:**

                `GET`
                
            *  **URL Params**

                None

            * **Data Params**

                None

            * **Error Response:**

                * **Code:** 404 NOT FOUND <br />
                **Content:** `{ error : "Matches doesn't exist" }`

                OR

                * **Code:** 401 UNAUTHORIZED <br />
                **Content:** `{ error : "You are unauthorized to make this request." }`

            * **Sample Call:**

                ```bash
                curl -H "Authorization: JWT <your_token>" -H "Content-Type: application/json" http://localhost:8000/api/elite_schedule/england/premier_league

                ```

        """
        matches = Match.objects.eng_premier_league()
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def conference(self, request):
        """
            Show all English Conference League matches.
            
            ----
            Returns json data about a list of matches from English Conference League Matches.
            =======================================

            * **URL**

                /england/conference

            * **Method:**

                `GET`
                
            *  **URL Params**

                None

            * **Data Params**

                None

            * **Error Response:**

                * **Code:** 404 NOT FOUND <br />
                **Content:** `{ error : "Matches doesn't exist" }`

                OR

                * **Code:** 401 UNAUTHORIZED <br />
                **Content:** `{ error : "You are unauthorized to make this request." }`

            * **Sample Call:**

                ```bash
                curl -H "Authorization: JWT <your_token>" -H "Content-Type: application/json" http://localhost:8000/api/elite_schedule/england/conference

                ```

        """
        matches = Match.objects.eng_conference()
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def league_1(self, request):
        """
            Show all English League 1 matches.
            
            ----
            Returns json data about a list of matches from English League 1 Matches.
            =======================================

            * **URL**

                /england/league_1

            * **Method:**

                `GET`
                
            *  **URL Params**

                None

            * **Data Params**

                None

            * **Error Response:**

                * **Code:** 404 NOT FOUND <br />
                **Content:** `{ error : "Matches doesn't exist" }`

                OR

                * **Code:** 401 UNAUTHORIZED <br />
                **Content:** `{ error : "You are unauthorized to make this request." }`

            * **Sample Call:**

                ```bash
                curl -H "Authorization: JWT <your_token>" -H "Content-Type: application/json" http://localhost:8000/api/elite_schedule/england/league_1

                ```

        """
        matches = Match.objects.eng_league_1()
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def league_2(self, request):
        """
            Show all English League 2 matches.
            
            ----
            Returns json data about a list of matches from English League 2 Matches.
            =======================================

            * **URL**

                /england/league_2

            * **Method:**

                `GET`
                
            *  **URL Params**

                None

            * **Data Params**

                None

            * **Error Response:**

                * **Code:** 404 NOT FOUND <br />
                **Content:** `{ error : "Matches doesn't exist" }`

                OR

                * **Code:** 401 UNAUTHORIZED <br />
                **Content:** `{ error : "You are unauthorized to make this request." }`

            * **Sample Call:**

                ```bash
                curl -H "Authorization: JWT <your_token>" -H "Content-Type: application/json" http://localhost:8000/api/elite_schedule/england/league_2

                ```

        """
        matches = Match.objects.eng_league_2()
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)
    
class SpainMatchesViewSet(viewsets.ViewSet,generics.ListAPIView):
    """
    A viewset that provides the standard action `GET`.
    """
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    def get_queryset(self, request):
        """
            Show all matches.
            ----
            Returns json data about a list of matches from Spanish Leagues.
            =======================================

            * **URL**

                /spain/

            * **Method:**

                `GET`
                
            *  **URL Params**

                None

            * **Data Params**

                None

            * **Success Response:**

                * **Code:** 200 <br />
                **Content:**` ADD CONTENT HERE`
            
            * **Error Response:**

                * **Code:** 404 NOT FOUND <br />
                **Content:** `{ error : "Matches doesn't exist" }`

                OR

                * **Code:** 401 UNAUTHORIZED <br />
                **Content:** `{ error : "You are unauthorized to make this request." }`

            * **Sample Call:**

                ```bash
                curl -H "Authorization: JWT <your_token>" -H "Content-Type: application/json" http://localhost:8000/api/elite_schedule/spain/

                ```

        """
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


class GermanyMatchesViewSet(viewsets.ViewSet,generics.ListAPIView):
    """
    A viewset that provides one standard action `GET`.
    """
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    def get_queryset(self, request):
        """
            Show all matches.
            ----
            Returns json data about a list of matches from German Leagues.
            =======================================

            * **URL**

                /germany/

            * **Method:**

                `GET`
                
            *  **URL Params**

                None

            * **Data Params**

                None

            * **Success Response:**

                * **Code:** 200 <br />
                **Content:**` ADD CONTENT HERE`
            
            * **Error Response:**

                * **Code:** 404 NOT FOUND <br />
                **Content:** `{ error : "Matches doesn't exist" }`

                OR

                * **Code:** 401 UNAUTHORIZED <br />
                **Content:** `{ error : "You are unauthorized to make this request." }`

            * **Sample Call:**

                ```bash
                curl -H "Authorization: JWT <your_token>" -H "Content-Type: application/json" http://localhost:8000/api/elite_schedule/germany/

                ```

        """
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

class ItalyMatchesViewSet(viewsets.ViewSet,generics.ListAPIView):
    """
    A viewset that provides one standard action `GET`.
    """
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    def get_queryset(self, request):
        """
            Show all matches.
            ----
            Returns json data about a list of matches from Italian Leagues.
            =======================================

            * **URL**

                /italy/

            * **Method:**

                `GET`
                
            *  **URL Params**

                None

            * **Data Params**

                None

            * **Success Response:**

                * **Code:** 200 <br />
                **Content:**` ADD CONTENT HERE`
            
            * **Error Response:**

                * **Code:** 404 NOT FOUND <br />
                **Content:** `{ error : "Matches doesn't exist" }`

                OR

                * **Code:** 401 UNAUTHORIZED <br />
                **Content:** `{ error : "You are unauthorized to make this request." }`

            * **Sample Call:**

                ```bash
                curl -H "Authorization: JWT <your_token>" -H "Content-Type: application/json" http://localhost:8000/api/elite_schedule/italy/

                ```

        """
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



