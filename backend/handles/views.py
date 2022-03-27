from .models import Handle
from .serializers import HandleSerializer
from rest_framework import viewsets


class HandleViewSet(viewsets.ModelViewSet):
    queryset = Handle.objects.all()
    serializer_class = HandleSerializer
