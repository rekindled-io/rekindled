from rest_framework import mixins, status, viewsets, generics
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend

from .models import Game, GameAndPlatform, Platform
from .serializers import GameSerializer, GameSimplifiedSerializer, PlatformSerializer

from .filters import GameFilter



class GameViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Game.objects.prefetch_related("platforms").order_by("name")
    serializer_class = GameSerializer
    filterset_class = GameFilter
    filter_backends = [DjangoFilterBackend, OrderingFilter]


class PlatformViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
    pagination_class = None
