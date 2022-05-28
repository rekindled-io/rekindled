from django.apps import apps
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.humanize.templatetags import humanize
from rest_framework import serializers

from games.models import Game, Platform
from handles.models import Handle
from handles.serializers import SlimHandleSerializer
from kindles.models import SeekingKindle
from kindles.serializers import SeekingKindleSerializer

from .models import Notification

User = get_user_model()


class GenericActionRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        model_type = value.actor

        if isinstance(model_type, Handle):
            serializer = SlimHandleSerializer(model_type)
            return serializer.data

        if isinstance(model_type, SeekingKindle):
            serializer = SeekingKindleSerializer(model_type)
            return serializer.data


class NotificationSerializer(serializers.ModelSerializer):
    sender = GenericActionRelatedField(read_only=True)
    recipient = GenericActionRelatedField(read_only=True)
    timestamp = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ["recipient", "timestamp", "sender", "message", "subject"]
        extra_kwargs = {
            "message": {"read_only": True},
        }

    def get_timestamp(self, obj):
        return humanize.naturaltime(obj.timestamp)

    def to_internal_value(self, data):
        object_id = data.pop("sender_object_id")
        content_type = data.pop("sender_content_type")

        ret = super().to_internal_value(data)

        ret["object_id"] = object_id
        ret["content_type"] = content_type

        return ret

    def validate(self, data):
        object_id = data.pop("sender_object_id")
        content_type = data.pop("sender_content_type")

        Model = apps.get_model(content_type)

        try:
            content_object = Model.objects.get(id=object_id)
        except Model.DoesNotExist:
            raise serializers.ValidationError("Not found")
        else:
            data["content_object"] = content_object

        return data
