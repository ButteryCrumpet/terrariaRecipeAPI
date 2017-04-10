from rest_framework import serializers
from recipeAPI.models import Item, Recipe, Ingredient

class ItemSerializer(serializers.ModelSerializer):
    #recipe = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Item
        fields = ('name', 'image')

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('item', 'amount')

class WriteableRecipeSerializer(serializers.Serializer):
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