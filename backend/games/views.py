from datetime import datetime, timedelta

from django.db.models import Count
from django.db.models.expressions import F, Window
from django.db.models.functions.window import Rank
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response

from .filters import GameFilter
from .models import Game, GameAndPlatform, Platform
from .serializers import (GameSerializer, GameSimplifiedSerializer,
                          PlatformSerializer)


class GameViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = (
        Game.objects.annotate(handle_count=Count("gameandplatform__handle"))
        .prefetch_related("platforms")
        .order_by("name")
    )
    serializer_class = GameSerializer
    filterset_class = GameFilter
    filter_backends = [DjangoFilterBackend, OrderingFilter]

    @action(detail=False, methods=["get"])
    def ranking(self, request):
        ranking = self.get_queryset().order_by("-handle_count")[:10]
        serializer = self.get_serializer(ranking, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    @action(detail=False, methods=["get"])
    def trending(self, request):
        dt = datetime.today()
        start_of_week = dt - timedelta(days=(dt.weekday() - 1) % 7)
        trending = (
            self.get_queryset()
            .filter(gameandplatform__handle__created__gt=start_of_week)
            .filter(handle_count__gt=0)
            .annotate(
                rank=Window(expression=Rank(), order_by=F("handle_count").desc())
            )[:10]
        )

        serializer = self.get_serializer(trending, many=True)

        return Response(serializer.data, status.HTTP_200_OK)


class PlatformViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
    pagination_class = None
