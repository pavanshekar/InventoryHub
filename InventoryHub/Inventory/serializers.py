from rest_framework import serializers
from .models import Item, Category, Tag

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['sku', 'name', 'category', 'tags', 'in_stock', 'available_stock']
        extra_kwargs = {
            'tags': {'required': False}
        }
