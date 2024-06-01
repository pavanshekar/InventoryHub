from django.test import TestCase
from .models import Category, Tag, Item

class CategoryModelTest(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(name='Test Category')
        self.assertEqual(category.name, 'Test Category')

class TagModelTest(TestCase):
    def test_tag_creation(self):
        tag = Tag.objects.create(name='Test Tag')
        self.assertEqual(tag.name, 'Test Tag')

class ItemModelTest(TestCase):
    def test_item_creation(self):
        category = Category.objects.create(name='Test Category')
        tag = Tag.objects.create(name='Test Tag')
        item = Item.objects.create(sku='Test SKU', name='Test Item', category=category, in_stock=10, available_stock=10)
        item.tags.add(tag)
        
        self.assertEqual(item.sku, 'Test SKU')
        self.assertEqual(item.name, 'Test Item')
        self.assertEqual(item.category.name, 'Test Category')
        self.assertIn(tag, item.tags.all())
