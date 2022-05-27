from django.urls.conf import path
from rest_framework import routers

from .views import HandleViewSet, HandleByUserViewSet

router = routers.SimpleRouter()
router.register(r"handles", HandleViewSet, "handle")

urlpatterns = [
    path(
        "handles/user/<str:user>/",
        HandleByUserViewSet.as_view({"get": "list"}),
        name="handle-user-list",
    ),
]