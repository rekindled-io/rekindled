from django.urls import include, path

from .views import (CookieTokenObtainPairView, CookieTokenRefreshView)


urlpatterns = [
    path("auth/token/", CookieTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", CookieTokenRefreshView.as_view(), name="token_refresh"),
]
