from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rekindled.permissions import AnonymousCreateAndOwnerUpdate
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.encoding import DjangoUnicodeDecodeError
from .utils import decode_uid, encode_uid
from rest_framework import status

from .serializers import UserSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    lookup_field = "username"
    permission_classes = [IsAuthenticatedOrReadOnly | AnonymousCreateAndOwnerUpdate]

    def get_object(self):
        user = self.kwargs.get("username")
        if user == "me":
            return self.request.user
        return super().get_object()

    def retrieve(self, request, username=None):
        if not request.user.is_authenticated and request.path == "/users/me/":
            return Response("401 Unauthorized", status=401)

        user = self.get_object()
        serializer = self.get_serializer(user)

        return Response(serializer.data, status=200)


class UserActivationView(APIView):
    def get(self, request, uid, token, format=None):
        try:
            decoded_username = decode_uid(uid)
            user = User.objects.get(username=decoded_username)
        except DjangoUnicodeDecodeError:
            return Response(
                {"status": "failed", "details": "Invalid user and/or token."},
                status=status.HTTP_404_NOT_FOUND,
            )

        if user.email_confirmed:
            return Response(
                {"status": "failed", "details": "Account is already activated."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not request.user.is_anonymous and request.user != user.username:
            return Response(
                {
                    "status": "failed",
                    "details": "This email link is intended for another user.",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not user.email_confirmed:
            user.email_confirmed = True
            user.save()

        return Response(
            {
                "status": "success",
                "details": "Your account has been successfully activated. You can now log in.",
            },
            status=status.HTTP_200_OK,
        )
