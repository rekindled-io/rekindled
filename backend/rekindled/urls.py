from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from users.urls import router as UserRouter

router = routers.SimpleRouter()

router.registry.extend(UserRouter.registry)

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
]
