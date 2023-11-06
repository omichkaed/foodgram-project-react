from django.contrib import admin

from recipes.models import (
    RecipeIngredient,
    Shopping_list,
    Ingredient,
    Favorite,
    Follow,
    Recipe,
    User,
    Tag
)


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'author',
    )
    search_fields = ('user__username', 'author__username')
    empty_value_display = '-пусто-'
    verbose_name = 'Подписки',


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'image',
        'text',
        'pub_date',
        'author'
    )
    search_fields = ('author__username', 'author__email', 'name')
    list_filter = ('tags',)
    empty_value_display = '-пусто-'
    verbose_name = 'Рецепты',
    inlines = (RecipeIngredientInline, )


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'measurement_unit'
    )
    search_fields = ('name', 'id')
    list_filter = ('measurement_unit',)
    empty_value_display = '-пусто-'
    verbose_name = 'Ингридиент',


@admin.register(Shopping_list)
class Shopping_listAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'recipe',
    )
    search_fields = ('user__username', 'user__email', 'recipe__name')
    list_filter = ('recipe__tags',)
    empty_value_display = '-пусто-'
    verbose_name = 'Список покупок',


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
        'color',
    )
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'
    verbose_name = 'Тег',


@admin.register(Favorite)
class FavoritesAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'recipe'
    )
    search_fields = ('user__username', 'user__email', 'recipe__name')
    list_filter = ('recipe__tags',)
    verbose_name = 'Избранное'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'is_staff',
        'is_superuser',
        'is_active'
    )
    list_filter = (
        ("is_staff", admin.BooleanFieldListFilter),
        ('is_superuser', admin.BooleanFieldListFilter),
        ('is_active', admin.BooleanFieldListFilter),
    )
    search_fields = ('username', 'email')
    empty_value_display = '-пусто-'
    verbose_name = 'Пользователь',
