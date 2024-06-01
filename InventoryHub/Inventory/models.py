from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Item(models.Model):
    sku = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='items')
    in_stock = models.IntegerField()
    available_stock = models.IntegerField()

    def __str__(self):
        return self.name
