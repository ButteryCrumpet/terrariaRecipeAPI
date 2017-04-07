from django.contrib import admin
from .models import Item, Ingredient, Recipe
# Register your models here.
admin.site.register(Item)
admin.site.register(Ingredient)
admin.site.register(Recipe)
