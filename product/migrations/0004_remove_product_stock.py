# Generated by Django 5.0.6 on 2024-06-20 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_productattributevalue_attribute_key_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
    ]
