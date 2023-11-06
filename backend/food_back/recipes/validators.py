from rest_framework import serializers


def validate_ingredients(self, ingredients):
    ingredients_list = []
    for ingredient in ingredients:
        ingredient_id = ingredient['id']
        if ingredient in ingredients_list:
            raise serializers.ValidationError(
                'You have already added this ingredient'
            )
        ingredients_list.append(ingredient_id)
    return ingredients
