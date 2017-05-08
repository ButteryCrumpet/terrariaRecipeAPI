from django.shortcuts import render
from django.http import Http404
from rest_framework import generics, permissions, mixins, status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from recipeAPI.models import Item, Recipe
from recipeAPI.serializers import WriteableRecipeSerializer, ItemSerializer, RecipeFullSerializer

import logging
logger = logging.getLogger('print')
# Create your views here.
class RecipeDetail(APIView):
    renderer_classes = (JSONRenderer,)

    def get_recipe(self, item):
        try:
            return Recipe.objects.get(item=item)
        except Recipe.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        recipe = self.get_recipe(pk)
        serializer = RecipeFullSerializer(recipe)
        return Response(serializer.data)

class RecipeCreate(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    parser_classes = (JSONParser,)

    def get_recipe(self, item):
        try:
            return Recipe.objects.get(item=item)
        except Recipe.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        serializer = WriteableRecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        recipe = self.get_recipe(pk)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ItemDetail(generics.RetrieveAPIView):
    renderer_classes = (JSONRenderer, )

    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemCreate(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    parser_classes = (JSONParser,)

    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ItemList(generics.ListAPIView):
    renderer_classes = (JSONRenderer, )

    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemSearch(APIView):
    renderer_classes = (JSONRenderer, )

    def get(self, request, search_term, format=None):
        items = Item.objects.filter(name__iregex=r'(' + search_term + ')+')
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

class RecipeSearch(APIView):
    renderer_classes = (JSONRenderer, )

    def get(self, request, search_term, format=None):
        items = Recipe.objects.filter(name__iregex=r'(' + search_term + ')+')
        serializer = RecipeFullSerializer(items, many=True)
        return Response(serializer.data)

#rewrite for creates
#one create update destroy view and one retrieve view
#use mixins for cud and generics for r
