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
    cover = serializers.URLField(read_only=True, source="game.cover.url")
    icon = serializers.URLField(read_only=True, source="game.icon.url")

    class Meta:
        model = GameAndPlatform
        fields = ["game_name", "platform_name", "cover", "icon"]


class GameSimplifiedSerializer(serializers.ModelSerializer):
    platforms = serializers.SlugRelatedField(
        slug_field="name", many=True, read_only=True
    )

    class Meta:
        model = Game
        fields = ["name", "platforms"]


class GameSerializer(GameSimplifiedSerializer):
    image = serializers.URLField(read_only=True, source="image.url")
    cover = serializers.URLField(read_only=True, source="cover.url")
    icon = serializers.URLField(read_only=True, source="icon.url")
    handle_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Game
        fields = GameSimplifiedSerializer.Meta.fields + [
            "image",
            "cover",
            "icon",
            "handle_count",
        ]
