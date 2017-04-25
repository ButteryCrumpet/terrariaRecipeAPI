from rest_framework import serializers
from recipeAPI.models import Item, Recipe, Ingredient

import logging
logger = logging.getLogger('print')

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('name', 'image')

class IngredientSerializer(serializers.ModelSerializer):

    def to_internal_value(self, data):
        return serializers.ModelSerializer.to_internal_value(self, data)

    class Meta:
        model = Ingredient
        fields = ('item', 'amount')

#must be pure dict/from JSON post request
class WriteableRecipeSerializer(serializers.ModelSerializer):
    item = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all())
    ingredients = IngredientSerializer(many=True)
    station = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all())

    def create(self, validated_data):
        ingredient_data = validated_data.pop('ingredients')
        recipe = Recipe.objects.create(**validated_data)

        for ingredient in ingredient_data:
            ingredient_item = Item.objects.get(name=ingredient['item'])
            amount = ingredient['amount']
            ingredient, created = Ingredient.objects.get_or_create(item=ingredient_item, amount=amount)
            recipe.ingredients.add(ingredient)

        return recipe

    class Meta:
        model = Recipe
        fields = ('item', 'amount', 'ingredients', 'station')

class IngredientFullSerializer(serializers.Serializer):
    item = ItemSerializer(read_only=True)
    amount = serializers.IntegerField()

    class Meta:
        model = Ingredient
        fields = ('item', 'amount')


class RecipeFullSerializer(serializers.Serializer):
    item = ItemSerializer(read_only=True)
    ingredients = IngredientFullSerializer(many=True, read_only=True)
    station = ItemSerializer(read_only=True)

    class Meta:
        model = Recipe
        fields = ('item', 'amount', 'ingredients', 'station')
