from django_filters import rest_framework as filters

from games.models import Game, Platform

from .models import Handle


class HandleFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    game = filters.ModelMultipleChoiceFilter(
        field_name="game_and_platform__game__name",
        lookup_expr="exact",
        queryset=Game.objects.all(),
        to_field_name="name",
    )
    platform = filters.ModelMultipleChoiceFilter(
        field_name="game_and_platform__platform__name",
        lookup_expr="exact",
        queryset=Platform.objects.all(),
        to_field_name="name",
    )
    ordering = filters.OrderingFilter(fields=["name", "game", "platform", "created"])

    class Meta:
        model = Handle
        fields = ["name", "platform", "game"]
