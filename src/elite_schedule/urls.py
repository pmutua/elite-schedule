from django.conf.urls import url
from elite_schedule import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'match_histories', views.MatchHistoryViewset, base_name='match')
router.register(r'england', views.EnglandMatchesViewSet, base_name='emgland')
router.register(r'spain', views.SpainMatchesViewSet, base_name='spain')
router.register(r'germany', views.GermanyMatchesViewSet, base_name='germany')
router.register(r'italy', views.ItalyMatchesViewSet, base_name='italy')



urlpatterns = router.urls