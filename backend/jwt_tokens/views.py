from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    TokenRefreshSerializer,
)
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .serializers import CookieTokenRefreshSerializer


class CookieTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]

    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get("refresh"):
            cookie_max_age = 3600 * 24 * 14
            response.set_cookie(
                "refresh_token",
                response.data["refresh"],
                # secure=True,
                samesite="strict",
                max_age=cookie_max_age,
                httponly=True,
            )
            del response.data["refresh"]
        return super().finalize_response(request, response, *args, **kwargs)


class CookieTokenRefreshView(TokenRefreshView):
    permission_classes = [AllowAny]
    serializer_class = CookieTokenRefreshSerializer

    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get("refresh"):
            cookie_max_age = 3600 * 24 * 14  # 14 days
            response.set_cookie(
                "refresh_token",
                response.data["refresh"],
                max_age=cookie_max_age,
                httponly=True,
            )
            del response.data["refresh"]
        return super().finalize_response(request, response, *args, **kwargs)


class LogoutView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request, *args):
        refresh_token_cookie = request.COOKIES.get("refresh_token")
        try:
            RefreshToken(refresh_token_cookie).blacklist()
        except TokenError:
            response = Response(status=status.HTTP_400_BAD_REQUEST)
            response.delete_cookie("refresh_token")
            response.delete_cookie("session-token")
            return response

        return Response(status=status.HTTP_204_NO_CONTENT)
