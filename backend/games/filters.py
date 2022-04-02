from django_filters import rest_framework as filters

from .models import Game, Platform


class GameFilter(filters.FilterSet):
    name = filters.ModelMultipleChoiceFilter(
        field_name="name",
        lookup_expr="icontains",
        queryset=Game.objects.all(),
        to_field_name="name",
    )
    platform = filters.ModelMultipleChoiceFilter(
        field_name="platforms__name",
        lookup_expr="exact",
        queryset=Platform.objects.all(),
        to_field_name="name",
    )

    class Meta:
        model = Game
        fields = ["name", "platform"]
