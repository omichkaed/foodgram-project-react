from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.db.models import Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers, viewsets, status, pagination
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    AllowAny
)
from rest_framework.response import Response
from rest_framework.decorators import action
from djoser.views import UserViewSet

from api.filters import IngredientFilter, RecipeFilter
from api.permissions import IsAuthorOrReadOnly
from api.serializers import (
    FollowValidateSerializer,
    RecipeCreateSerializers,
    RecipeShortSerializer,
    IngredientSerializer,
    FollowSerializer,
    RecipeSerializer,
    UserSerializer,
    TagSerializer,
)
from recipes.models import (
    RecipeIngredient,
    ShoppingList,
    Ingredient,
    Favorite,
    Follow,
    Recipe,
    Tag,
)
from recipes.constants import (
    FILE_SHOPPING_LIST,
    CONTENT,
)


User = get_user_model()


class CustomUserViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )

    @action(
        detail=True,
        methods=('post',),
        permission_classes=(IsAuthenticatedOrReadOnly,)
    )
    def subscribe(self, request, id=None):
        user = request.user
        author = get_object_or_404(User, id=id)
        data = {'user': request.user.id, 'author': id}
        follow = Follow.objects.create(user=user, author=author)
        serializer = FollowValidateSerializer(
            follow,
            data=data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @subscribe.mapping.delete
    def unsubscribe(self, request, id):
        follow = Follow.objects.filter(
            user=request.user,
            author=get_object_or_404(User, id=id),
        )
        if not follow.exists():
            raise serializers.ValidationError('There is no such subscription')
        follow.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(
        detail=False,
        permission_classes=(IsAuthenticatedOrReadOnly, ),
        serializer_class=(FollowSerializer, )
    )
    def subscriptions(self, request):
        queryset = request.user.followers.all()
        pages = self.paginate_queryset(queryset)
        serializer = FollowSerializer(
            pages,
            many=True,
            context={'request': request}
        )
        return self.get_paginated_response(serializer.data)


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RecipeFilter
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)
    pagination_class = pagination.PageNumberPagination

    def get_serializer_class(self):
        if self.action in ('retrive', 'list'):
            return RecipeSerializer
        return RecipeCreateSerializers

    @staticmethod
    def __add_to(model, user, pk):
        recipe = get_object_or_404(Recipe, id=pk)
        model.objects.create(user=user, recipe=recipe)
        serializer = RecipeShortSerializer(recipe)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @staticmethod
    def __delete_from(model, user, pk):
        model.objects.filter(user=user, recipe__id=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @staticmethod
    def __create_txt_cart(ingredients):
        shopping_list = 'Shopping list'
        for ingredient in ingredients:
            shopping_list += (
                f"\n{ingredient['ingredient__name']} "
                f"({ingredient['ingredient__measurement_unit']}) - "
                f"{ingredient['amount']}"
            )
        return shopping_list

    @action(detail=True, methods=['post', 'delete'])
    def favorite(self, request, pk):
        if request.method == 'POST':
            return self.__add_to(Favorite, request.user, pk)
        return self.__delete_from(Favorite, request.user, pk)

    @action(detail=True, methods=['post', 'delete'])
    def shopping_cart(self, request, pk):
        if request.method == 'POST':
            return self.__add_to(ShoppingList, request.user, pk)
        return self.__delete_from(ShoppingList, request.user, pk)

    @action(detail=False, methods=('GET', ))
    def download_shopping_cart(self, request):
        ingredients = RecipeIngredient.objects.filter(
            recipe__shopping_lists__user=request.user
        ).order_by('ingredient__name').values(
            'ingredient__name',
            'ingredient__measurement_unit'
        ).annotate(amount=Sum('amount'))
        shoppiing_list = self.__create_txt_cart(ingredients)
        response = HttpResponse(shoppiing_list, content_type=CONTENT)
        response['Content-Disposition'] = "attachment; "
        f"filename='{FILE_SHOPPING_LIST}'"
        return response


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    pagination_class = None
    permission_classes = (AllowAny,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = IngredientFilter


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (AllowAny,)
    pagination_class = None
