from django.urls.conf import path
from rest_framework import routers

from .views import UserActivationView, UserViewSet

router = routers.SimpleRouter()
router.register(r"users", UserViewSet, "user")

urlpatterns = [
    path(
        "activate/<uid>/<token>/", UserActivationView.as_view(), name="users-activate"
    ),
]
