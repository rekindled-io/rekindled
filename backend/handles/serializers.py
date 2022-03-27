from django.contrib.auth import get_user_model
from rest_framework import serializers

from games.models import Game, GameAndPlatform, Platform
from games.serializers import GameAndPlatformSerializer

from .models import Handle

User = get_user_model()


class HandleSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field="username",
        required=True,
        allow_null=False,
        queryset=User.objects.all(),
    )
    game_and_platform = GameAndPlatformSerializer()
    start_period = serializers.SerializerMethodField()
    end_period = serializers.SerializerMethodField()

    class Meta:
        model = Handle
        fields = "__all__"
        read_only_fields = [
            "id",
            "created",
            "user",
            "start_period",
            "end_period",
            "region",
        ]

    def get_start_period(self, obj):
        return obj.start_period.year if obj.start_period else None

    def get_end_period(self, obj):
        return obj.end_period.year if obj.end_period else None
