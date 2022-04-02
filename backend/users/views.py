from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rekindled.permissions import AnonymousCreateAndOwnerUpdate
from rest_framework.response import Response


from .serializers import UserSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "username"
    permissions = [IsAuthenticatedOrReadOnly | AnonymousCreateAndOwnerUpdate]

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
