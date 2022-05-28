from django.contrib.admin.options import get_content_type_for_model
from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from handles.models import Handle

from .models import Notification
from .serializers import NotificationSerializer

User = get_user_model()


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = User.objects.get(username=self.request.user.get_username())
        for notification in self.queryset:
            if isinstance(notification.sender.actor, Handle):
                self.queryset.filter(recipient__handle__user=user)
        return self.queryset.order_by("-timestamp")
