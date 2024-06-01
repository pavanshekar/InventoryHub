from django.db import migrations

def add_initial_categories_and_tags(apps, schema_editor):
    Category = apps.get_model('Inventory', 'Category')
    Tag = apps.get_model('Inventory', 'Tag')

    # Initial Categories
    category_names = ['Bundles', 'Finished products', 'Raw materials']
    for name in category_names:
        Category.objects.create(name=name)

    # Initial Tags
    tag_names = ['Etsy', 'Xero', 'Shopify']
    for name in tag_names:
        Tag.objects.create(name=name)

class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0001_initial'),  
    ]

    operations = [
        migrations.RunPython(add_initial_categories_and_tags),
    ]
