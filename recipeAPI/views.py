from django.shortcuts import render
from django.http import Http404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from recipeAPI.models import Item, Recipe, Ingredient
from recipeAPI.serializers import WriteableRecipeSerializer, ItemSerializer, RecipeFullSerializer

# Create your views here.
class RecipeDetail(APIView):
    
    def get_recipe(self, item):
        try:
            return Recipe.objects.get(item=item)
        except Recipe.DoesNotExist:
            raise Http404

    def get(self, request, pk, format='json'):
        recipe = self.get_recipe(pk)
        serializer = RecipeFullSerializer(recipe)
        return Response(serializer.data)

    def put(self, request, pk, format='json'):
        recipe = self.get_recipe(pk)
        serializer = WriteableRecipeSerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format='json'):
        recipe = self.get_recipe(pk)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemList(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemSearch(APIView):

    def get(self, request, search_term, format='json'):
        items = Item.objects.filter(name__iregex=r'^(' + search_term + ')+')
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

