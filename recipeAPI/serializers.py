from rest_framework import serializers
from recipeAPI.models import Item, Recipe, Ingredient

class ItemSerializer(serializers.ModelSerializer):
    #recipe = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Item
        fields = ('name', 'image', 'is_station')

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('item', 'amount')

class RecipeSerializer(serializers.Serializer):
    item = ItemSerializer(read_only=True)
    ingredients = IngredientSerializer(many=True)
    station = ItemSerializer(read_only=True)

    def create(self, validated_data):
        ingredient_data = validated_data.pop('ingredients')
        item_data = validated_data.pop('item')
        recipe = Recipe.objects.create(**validated_data)
        recipe.item = Item.objects.get(item_data['name'])
        for ingredient in indgredient_data:
            ingredient_item = Item.objects.get(ingredient['item'])
            amount = ingredient['amount']
            ingredient, created = Ingredient.objects.get_or_create(item=ingredient_item, amount=amount)
            recipe.ingredients.add(ingredient)

        return recipe

    class Meta:
        model = Recipe
        fields = ('item', 'amount', 'ingredients', 'station')
