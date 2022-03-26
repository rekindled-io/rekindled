from rest_framework import mixins, status, viewsets, generics
from rest_framework.decorators import action

from .models import Game, GameAndPlatform, Platform
from .serializers import (GameSerializer, GameSimplifiedSerializer,
                          PlatformSerializer)



class GameViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Game.objects.prefetch_related("platforms").order_by("name")
    serializer_class = GameSerializer


class PlatformViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
    pagination_class = None
