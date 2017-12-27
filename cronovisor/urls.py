from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from cronovisor import views
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'image', views.ImageViewSet)
router.register(r'street', views.StreetViewSet)
router.register(r'marker', views.MarkerViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),	
]
