from django.urls.conf import path
from rest_framework import routers

from .views import GameViewSet, PlatformViewSet

router = routers.SimpleRouter()
router.register(r"games", GameViewSet)
router.register(r"platforms", PlatformViewSet)
