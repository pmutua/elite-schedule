from django.conf.urls import url
from elite_schedule import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'match_histories', views.MatchHistoryViewset, base_name='match')
router.register(r'england', views.EnglandViewSet, base_name='match')


urlpatterns = router.urls