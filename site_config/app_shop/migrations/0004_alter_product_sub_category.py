# Generated by Django 4.1.6 on 2023-02-12 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_shop', '0003_alter_product_sub_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sub_category',
            field=models.ManyToManyField(to='app_shop.subcategory', verbose_name='Под категория'),
        ),
    ]