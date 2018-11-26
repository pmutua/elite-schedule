from django.conf.urls import url
from elite_schedule import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'match_histories', views.MatchHistoryViewset, base_name='match')
router.register(r'england', views.EnglandViewSet, base_name='emgland')
router.register(r'spain', views.SpainViewSet, base_name='spain')
router.register(r'germany', views.GermanyViewSet, base_name='germany')
router.register(r'italy', views.SpainViewSet, base_name='italy')



urlpatterns = router.urls