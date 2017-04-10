from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    image = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return self.item.name + '(' + str(self.amount) + ')'

class Recipe(models.Model):
    item = models.OneToOneField(Item, related_name='recipe', on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
    ingredients = models.ManyToManyField(Ingredient)
    station = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='as_station')

    def __str__(self):
        return 'Recipe: ' + str(self.item)