from django.test import TestCase

MY_AUTH_TOKEN = '1ea7ec39a27be022a048ffde1dd4ed7d7ebb4e47'

# Create your tests here.
def test1():
    from recipeAPI.models import Recipe
    from recipeAPI.serializers import WriteableRecipeSerializer
    data = {'item': 'sex', 'ingredients':[{'item':'my_penis', 'amount':1}, {'item': 'boobs', 'amount': 1}], 'station':'boobs'}
    inst = Recipe.objects.get(item='sex')
    s = WriteableRecipeSerializer(inst, data=data)
    return s


def test2():
    from recipeAPI.models import Item
    from recipeAPI.serializers import ItemSerializer

    r = Item.objects.all()
    return ItemSerializer(r[0])

def test3():
    from recipeAPI.models import Recipe
    from recipeAPI.serializers import RecipeSerializer
    from rest_framework.renderers import JSONRenderer
    from rest_framework.parsers import JSONParser
    from django.utils.six import BytesIO

    r = Recipe.objects.get()
    r = RecipeSerializer(r)
    r = JSONRenderer().render(r.data)
    r = BytesIO(r)
    r = JSONParser().parse(r)

    print(r)
    s = RecipeSerializer(data=r)
    Recipe.objects.all().delete()

    if s.is_valid():
        s.save()
    else:
        print('you dun goofed')

def test4():
    import requests
    import json
    url = 'http://127.0.0.1:8000/manager/recipe/sex/'
    headers = {'Authorization': 'Token 1ea7ec39a27be022a048ffde1dd4ed7d7ebb4e47', 'Content-Type':'application/json'}
    raw_data = {'item': 'sex', 'ingredients':[{'item':'my_penis', 'amount':1}], 'station':'boobs'}
    data = json.dumps(raw_data)
    r = requests.post(url, headers=headers, data=data)
    return r


def delete_all(item=True, recipe=True, ingredient=True):
    from recipeAPI.models import Recipe, Ingredient, Item

    if item == True:
        Item.objects.all().delete()
    if recipe == True:
        Recipe.objects.all().delete()
    if ingredient == True:
        Ingredient.objects.all().delete()

def remake_example():
    from recipeAPI.models import Recipe, Ingredient, Item

    a = Item.objects.get_or_create(name='my penis', image='dick.pic')
    b = Item.objects.get_or_create(name='boobs', image='rack.jpg')
    c = Item.objects.get_or_create(name='orgasm', image='o.face')
    d = Item.objects.get_or_create(name='back alley', image='dump.ster')

    i1 = Ingredient.objects.get_or_create(item=a[0], amount=1)
    i2 = Ingredient.objects.get_or_create(item=b[0], amount=2)

    r = Recipe.objects.create(
        item=c[0],
        amount=200,
        station=d[0]
    )

    r.ingredients.add(i1[0])
    r.ingredients.add(i2[0])
