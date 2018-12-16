from django.conf.urls import url
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'matches', views.MatchHistoryViewset, base_name='match')
router.register(r'team/search/', views.TeamSearchAPIView, base_name='team_search')
router.register(r'england', views.EnglandMatchesViewSet, base_name='emgland')
router.register(r'spain', views.SpainMatchesViewSet, base_name='spain')
router.register(r'germany', views.GermanyMatchesViewSet, base_name='germany')
router.register(r'italy', views.ItalyMatchesViewSet, base_name='italy')



urlpatterns = router.urls