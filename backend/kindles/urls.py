from django.urls.conf import path
from rest_framework import routers

from .views import DirectKindleViewSet, SeekingKindleViewSet

router = routers.SimpleRouter()
router.register("kindles/direct", DirectKindleViewSet)
router.register("kindles/seeking", SeekingKindleViewSet)
