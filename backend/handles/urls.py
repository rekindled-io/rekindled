from django.urls.conf import path
from rest_framework import routers

from .views import HandleViewSet

router = routers.SimpleRouter()
router.register(r"handles", HandleViewSet, "handle")
