from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('matches/', views.MatchHistoryViewset.as_view({'get': 'list'}), name='match'),
    path('team/search/', views.TeamSearchAPIView.as_view({'get': 'list'}), name='team_search'),
    path('england/', views.EnglandMatchesViewSet.as_view({'get': 'list'}), name='emgland'),
    path('spain/', views.SpainMatchesViewSet.as_view({'get': 'list'}), name='spain'),
    path('germany/', views.GermanyMatchesViewSet.as_view({'get': 'list'}), name='germany'),
    path('italy/', views.ItalyMatchesViewSet.as_view({'get': 'list'}), name='italy')

]
