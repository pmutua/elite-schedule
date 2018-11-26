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
        Returns json data about a list of matches from all League Divisions.
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
            curl -H "Authorization: JWT <your_token>" -H "Content-Type: application/json" http://localhost:8000/api/elite_schedule/matches

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
        Show all English Divisions matches.
        
        ----
        Returns json data about a list of matches from all English Divisions.
        =======================================

        * **URL**

            /england

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
            curl -H "Authorization: JWT <your_token>" -H "Content-Type: application/json" http://localhost:8000/api/elite_schedule/england

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
            Returns json data about a list of matches from English Premier League Division matches.
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
            Show all English Conference Division.
            
            ----
            Returns json data about a list of matches from English Conference Division matches.
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
            Returns json data about a list of matches from English League 1 Division.
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
            Returns json data about a list of matches from English League 2 Division.
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
        Show all Spanish Divisions matches.
        
        ----
        Returns json data about a list of matches from Spanish League Divisions.
        =======================================

        * **URL**

            /spain

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
            curl -H "Authorization: JWT <your_token>" -H "Content-Type: application/json" http://localhost:8000/api/elite_schedule/spain

            ```

    """

    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    def get_queryset(self, request):
        queryset = Match.objects.filter(
                Q(division__icontains="SP1")|
                Q(division__icontains="SP2")
                )
        serializer = MatchSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def la_liga_primiera(self, request):
        """
            Show all La Liga Primiera matches.
            
            ----
            Returns json data about a list of matches from La Liga Primiera Division.
            =======================================

            * **URL**

                /spain/la_liga_primiera

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
                curl -H "Authorization: JWT <your_token>" -H "Content-Type: application/json" http://localhost:8000/api/elite_schedule/england/spain/la_liga_primiera

                ```

        """
        matches = Match.objects.la_liga_primiera()
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def la_liga_segunda(self, request):
        """
            Show all Liga Segunda matches.
            
            ----
            Returns json data about a list of matches from la Liga Segunda Division.
            =======================================

            * **URL**

                /spain/la_liga_segunda
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
                curl -H "Authorization: JWT <your_token>" -H "Content-Type: application/json" http://localhost:8000/api/elite_schedule/england/spain/la_liga_segunda

                ```

        """
        matches = Match.objects.accepted()
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)


class GermanyMatchesViewSet(viewsets.ViewSet,generics.ListAPIView):
    """
        Show all German Divisions matches.
        
        ----
        Returns json data about a list of matches from German Divisions.
        =======================================

        * **URL**

            /germany

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
            curl -H "Authorization: JWT <your_token>" -H "Content-Type: application/json" http://localhost:8000/api/elite_schedule/germany

            ```

    """
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    def get_queryset(self, request):
        queryset = Match.objects.filter(
                Q(division__icontains="D1")|
                Q(division__icontains="D2")
                )
        serializer = MatchSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def bundesliga_1(self, request):
        """
            Show all Bundesliga 1 matches.
            
            ----
            Returns json data about a list of matches from Bundesliga 1 Division.
            =======================================

            * **URL**

                /germany/bundesliga_1

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
                curl -H "Authorization: JWT <your_token>" -H "Content-Type: application/json" http://localhost:8000/api/elite_schedule/germany/bundesliga_1

                ```

        """
        matches = Match.objects.bundesliga_1()
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def bundesliga_2(self, request):
        """
            Show all Bundesliga 2 matches.
            
            ----
            Returns json data about a list of matches from Bundesliga 2 Division.
            =======================================

            * **URL**

                /germany/bundesliga_2

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
                curl -H "Authorization: JWT <your_token>" -H "Content-Type: application/json" http://localhost:8000/api/elite_schedule/germany/bundesliga_2

                ```

        """
        matches = Match.objects.bundesliga_2()
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)

class ItalyMatchesViewSet(viewsets.ViewSet,generics.ListAPIView):
    """
        Show all Italian Divisions matches.
        
        ----
        Returns json data about a list of matches from Italian Divisions.
        =======================================

        * **URL**

            /italy

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
            curl -H "Authorization: JWT <your_token>" -H "Content-Type: application/json" http://localhost:8000/api/elite_schedule/italy

            ```

    """
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    def get_queryset(self, request):
       
        queryset = Match.objects.filter(
                Q(division__icontains="I1")|
                Q(division__icontains="I2")
                )
        serializer = MatchSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def seria_a(self, request):
        """
            Show all Seria A matches.
            
            ----
            Returns json data about a list of matches from Seria A Division.
            =======================================

            * **URL**

                /italy/seria_a

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
                curl -H "Authorization: JWT <your_token>" -H "Content-Type: application/json" http://localhost:8000/api/elite_schedule/italy/seria_a/

                ```

        """
        matches = Match.objects.seria_a()
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def seria_b(self, request):
        """
            Show all Seria B matches.
            
            ----
            Returns json data about a list of matches from Seria B Division.
            =======================================

            * **URL**

                /italy/seria_b

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
                curl -H "Authorization: JWT <your_token>" -H "Content-Type: application/json" http://localhost:8000/api/elite_schedule/italy/seria_b

                ```

        """
        matches = Match.objects.seria_b()
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)



