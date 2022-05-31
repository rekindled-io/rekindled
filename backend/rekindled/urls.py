from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from jwt_tokens.urls import urlpatterns as TokenURL
from users.urls import router as UserRouter
from games.urls import router as GameRouter
from handles.urls import router as HandleRouter
from kindles.urls import router as KindleRouter
from notifications.urls import router as NotificationRouter

router = routers.SimpleRouter()

router.registry.extend(UserRouter.registry)
router.registry.extend(GameRouter.registry)
router.registry.extend(HandleRouter.registry)
router.registry.extend(KindleRouter.registry)
router.registry.extend(NotificationRouter.registry)

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path("", include("users.urls")),
] + TokenURL

if settings.DEBUG:

    urlpatterns = (
        urlpatterns
        + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )
