from django.urls import include, path, re_path
from rest_framework import routers

from api.views import (
    IngredientViewSet,
    CustomUserViewSet,
    RecipeViewSet,
    TagViewSet
)


router = routers.DefaultRouter()


router.register('recipes', RecipeViewSet, basename='recipes')
router.register('users', CustomUserViewSet, basename='users')
router.register('tags', TagViewSet, basename='tag')
router.register('ingredients', IngredientViewSet, basename='ingredients')

urlpatterns = [
    path('', include(router.urls)),
    re_path('auth/', include('djoser.urls.authtoken')),
]
