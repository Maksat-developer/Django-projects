# Generated by Django 4.1.6 on 2023-02-16 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_shop', '0008_alter_category_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sub_category',
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]
