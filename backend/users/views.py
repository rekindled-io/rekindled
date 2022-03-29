from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rekindled.permissions import AnonymousCreateAndOwnerUpdate


from .serializers import UserSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "username"
    permissions = [IsAuthenticatedOrReadOnly | AnonymousCreateAndOwnerUpdate]