from .models import Handle
from .serializers import HandleSerializer
from rest_framework import viewsets, status, mixins
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework.decorators import action

from .filters import HandleFilter
from django_filters.rest_framework.backends import DjangoFilterBackend


class CreateListMixin:
    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get("data", {}), list):
            kwargs["many"] = True

        return super().get_serializer(*args, **kwargs)


class HandleViewSet(CreateListMixin, viewsets.ModelViewSet):
    queryset = Handle.objects.all()
    serializer_class = HandleSerializer
    filterset_class = HandleFilter
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        qs = self.queryset.select_related(
            "user",
            "game_and_platform__game",
            "game_and_platform__platform",
        )

        # Don't return user's own handles in results
        if self.request.user.is_authenticated and not self.request.query_params.get("includeSelf"):
            qs = qs.exclude(user=self.request.user)

        return qs

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            content = {"name": ["A handle with that name already exists."]}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["get"], )
    def recent(self, request):
        qs = self.get_queryset().order_by("created")
        filtered_qs = self.filter_queryset(qs)[:5]
        serializer = self.get_serializer(filtered_qs, many=True)

        return Response(serializer.data, status.HTTP_200_OK)
