from django.urls import path, include
from rest_framework import routers

from musician.views import MusicianViewSet

router = routers.DefaultRouter()
router.register("manage-list", MusicianViewSet, basename="manage")

urlpatterns = [
    path("musician/", include(router.urls))
]

app_name = "musician"
