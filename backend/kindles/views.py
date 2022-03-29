from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import DirectKindle, SeekingKindle
from .serializers import DirectKindleSerializer, SeekingKindleSerializer


class DirectKindleViewSet(viewsets.ModelViewSet):
    queryset = DirectKindle.objects.all()
    serializer_class = DirectKindleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.select_related(
            "source_user", "source_handle", "handle"
        ).filter(source_user=self.request.user)


class SeekingKindleViewSet(viewsets.ModelViewSet):
    queryset = SeekingKindle.objects.all()
    serializer_class = SeekingKindleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.select_related("source_user", "source_handle").filter(
            source_user=self.request.user
        )
