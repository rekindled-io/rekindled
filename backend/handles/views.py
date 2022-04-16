from .models import Handle
from .serializers import HandleSerializer
from rest_framework import viewsets


class HandleViewSet(viewsets.ModelViewSet):
    queryset = Handle.objects.all()
    serializer_class = HandleSerializer

    def get_queryset(self):
        qs = self.queryset.select_related(
            "user",
            "game_and_platform__game",
            "game_and_platform__platform",
        )

        # Don't return user's own handles in results
        if self.request.user.is_authenticated and self.action == "list":
            qs = qs.exclude(user=self.request.user)

        return qs
