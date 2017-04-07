from django.test import TestCase

# Create your tests here.
def test1():
    from recipeAPI.models import Recipe
    from recipeAPI.serializers import RecipeSerializer

    r = Recipe.objects.get()
    return [RecipeSerializer(r), r]

def test2():
    from recipeAPI.models import Item
    from recipeAPI.serializers import ItemSerializer

    r = Item.objects.all()
    return ItemSerializer(r[0])

def test3():
    from recipeAPI.models import Recipe
    from recipeAPI.serializers import RecipeSerializer

    data = {
        'ingredients': [{'item': 'boobs', 'amount': 3}, {'item': 'my penis', 'amount': 1}],
        'item': {'name': 'super orgasms'},
        'station': {'name': 'back alley'},
    }

    f = RecipeSerializer(data=data)
    if f.is_valid():
        f.save()
    else:
        print('you dun goofed')

def delete_all():
    from recipeAPI.models import Recipe, Ingredient, Item

    Item.objects.all().delete()
    Recipe.objects.all().delete()
    Ingredient.objects.all().delete()

def remake_example():
    from recipeAPI.models import Recipe, Ingredient, Item

    a = Item.objects.create(name='my penis', image='dick.pic', is_station=False)
    b = Item.objects.create(name='boobs', image='rack.jpg', is_station=False)
    c = Item.objects.create(name='orgasm', image='o.face', is_station=False)
    d = Item.objects.create(name='back alley', image='dump.ster', is_station=True)

    i1 = Ingredient.objects.create(item=b, amount=2)
    i2 = Ingredient.objects.create(item=a, amount=1)
    
    r = Recipe.objects.create(
        item=c,
        amount=200,
        station=d
    )

    r.ingredients.add(i1)
    r.ingredients.add(i2)
