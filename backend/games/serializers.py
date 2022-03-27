from collections import defaultdict

from rest_framework import serializers

from .models import Game, GameAndPlatform, Platform


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ["name"]


class GameAndPlatformSerializer(serializers.ModelSerializer):
    game_name = serializers.SlugRelatedField(
        source="game", queryset=Game.objects.all(), required=True, slug_field="name"
    )
    platform_name = serializers.SlugRelatedField(
        source="platform",
        queryset=Platform.objects.all(),
        required=True,
        slug_field="name",
    )

    class Meta:
        model = GameAndPlatform
        fields = ["game_name", "platform_name"]


class GameSimplifiedSerializer(serializers.ModelSerializer):
    platforms = serializers.SlugRelatedField(
        slug_field="name", many=True, read_only=True
    )

    class Meta:
        model = Game
        fields = ["name", "platforms"]


class GameSerializer(GameSimplifiedSerializer):
    class Meta:
        model = Game
        fields = GameSimplifiedSerializer.Meta.fields
