from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from jwt_tokens.urls import urlpatterns as TokenURL
from users.urls import router as UserRouter
from games.urls import router as GameRouter
from handles.urls import router as HandleRouter
from kindles.urls import router as KindleRouter

router = routers.SimpleRouter()

router.registry.extend(UserRouter.registry)
router.registry.extend(GameRouter.registry)
router.registry.extend(HandleRouter.registry)
router.registry.extend(KindleRouter.registry)

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
] + TokenURL
