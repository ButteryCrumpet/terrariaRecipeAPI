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
    item = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all())
    ingredients = IngredientSerializer(many=True)
    station = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all())

    def create(self, validated_data):
        ingredient_data = validated_data.pop('ingredients')
        recipe = Recipe.objects.create(**validated_data)
        for ingredient in ingredient_data:
            ingredient_item = Item.objects.get(name=ingredient['item'])
            amount = ingredient['amount']
            ingredient = Ingredient.objects.get_or_create(item=ingredient_item, amount=amount)
            recipe.ingredients.add(ingredient[0])

        return recipe

    class Meta:
        model = Recipe
        fields = ('item', 'amount', 'ingredients', 'station')
