from django.contrib.auth import get_user_model
from rest_framework import serializers

from games.models import Game, GameAndPlatform, Platform
from games.serializers import GameAndPlatformSerializer
from handles.models import Handle
from handles.serializers import HandleSerializer

from .models import BaseKindle, DirectKindle, SeekingKindle

User = get_user_model()


class KindleBaseSerializer(serializers.ModelSerializer):
    source_user = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True,
        default=serializers.CurrentUserDefault(),
    )
    source_handle = serializers.SlugRelatedField(
        slug_field="name", allow_null=False, read_only=True
    )

    class Meta:
        model = BaseKindle
        abstract = True
        fields = [
            "source_user",
            "source_handle",
            "message",
        ]


class SeekingKindleSerializer(KindleBaseSerializer):
    game_and_platform = GameAndPlatformSerializer()

    class Meta:
        model = SeekingKindle
        fields = KindleBaseSerializer.Meta.fields + ["handle", "game_and_platform"]

    def create(self, validated_data):
        instance = None
        game_and_platform = validated_data.pop("game_and_platform")
        if "source_user" not in validated_data:
            validated_data["source_user"] = self.context["request"].user
        try:
            instance = SeekingKindle(
                **validated_data,
                game_and_platform=GameAndPlatform.objects.get(
                    game=game_and_platform["game"],
                    platform=game_and_platform["platform"],
                ),
            )
            instance.save()
        except GameAndPlatform.DoesNotExist:
            raise serializers.ValidationError(
                {"detail": "Game and platform combination is not valid."}
            )

        return instance


class DirectKindleSerializer(KindleBaseSerializer):
    handle = serializers.SlugRelatedField(slug_field="name", read_only=True)
    handle_id = serializers.PrimaryKeyRelatedField(
        source="handle",
        queryset=Handle.objects.all(),
        write_only=True,
        required=True,
    )

    class Meta:
        model = DirectKindle
        fields = KindleBaseSerializer.Meta.fields + ["handle", "handle_id"]

    def create(self, validated_data):
        if "source_user" not in validated_data:
            validated_data["source_user"] = self.context["request"].user

        return super().create(validated_data)
