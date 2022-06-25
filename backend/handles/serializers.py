from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.humanize.templatetags import humanize

from games.models import Game, GameAndPlatform, Platform
from games.serializers import GameAndPlatformSerializer

from rekindled.converters import HashidsConverter

from .models import Handle

User = get_user_model()


class BulkCreateListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        result = [self.child.create(attrs) for attrs in validated_data]

        try:
            self.child.Meta.model.objects.bulk_create(result)
        except IntegrityError as e:
            raise ValidationError(e)

        return result


class SlimHandleSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field="username",
        required=True,
        allow_null=False,
        queryset=User.objects.all(),
    )
    game_and_platform = GameAndPlatformSerializer()

    class Meta:
        model = Handle
        fields = ["id", "user", "game_and_platform"]


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
    timestamp = serializers.SerializerMethodField()

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
            "timestamp",
            "game",
        ]
        list_serializer_class = BulkCreateListSerializer

    def validate_game_and_platform(self, value):
        try:
            GameAndPlatform.objects.get(
                game=value["game"],
                platform=value["platform"],
            )
        except GameAndPlatform.DoesNotExist:
            raise serializers.ValidationError(
                {"detail": "The game/platform doesn't exist."}
            )

        return value

    def create(self, validated_data):
        game_and_platform = validated_data.pop("game_and_platform")

        instance = Handle(
            **validated_data,
            game_and_platform=GameAndPlatform.objects.get(
                game=game_and_platform["game"],
                platform=game_and_platform["platform"],
            )
        )

        if isinstance(self._kwargs["data"], dict):
            instance.save()

        return instance

    def to_representation(self, instance):
        res = super().to_representation(instance)
        res["id"] = HashidsConverter.encode_id(res["id"])

        return res

    def get_start_period(self, obj):
        return obj.start_period.year if obj.start_period else None

    def get_end_period(self, obj):
        return obj.end_period.year if obj.end_period else None

    def get_timestamp(self, obj):
        return humanize.naturaltime(obj.created)
