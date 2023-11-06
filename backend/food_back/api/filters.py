from django_filters.rest_framework import FilterSet, filters

from recipes.models import Ingredient, Recipe


class IngredientFilter(FilterSet):
    name = filters.CharFilter(lookup_expr='startswith')

    class Meta:
        model = Ingredient
        fields = ('name',)


class RecipeFilter(FilterSet):
    tags = filters.AllValuesMultipleFilter(field_name='tags__slug')
    is_favorited = filters.BooleanFilter(method='is_favorited_filter')
    is_in_shopping_cart = filters.BooleanFilter(
        method='is_in_shopping_cart_filter'
    )

    class Meta:
        model = Recipe
        fields = ('tags', 'author')

    def is_favorited_filter(self, queryset, name, value):
        user = self.request.user.pk
        if value:
            return queryset.filter(favorites__user=user)
        return queryset

    def is_in_shopping_cart_filter(self, queryset, name, value):
        user = self.request.user.pk
        if value:
            return queryset.filter(sllists__user=user)
        return queryset
