from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from jwt_tokens.urls import urlpatterns as TokenURL
from users.urls import router as UserRouter
from games.urls import router as GameRouter
from handles.urls import router as HandleRouter

router = routers.SimpleRouter()

router.registry.extend(UserRouter.registry)
router.registry.extend(GameRouter.registry)
router.registry.extend(HandleRouter.registry)

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
] + TokenURL
