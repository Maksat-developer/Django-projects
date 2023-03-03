# Generated by Django 4.1.6 on 2023-02-12 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='category')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_shop.category', verbose_name='')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name in product:')),
                ('description', models.TextField(verbose_name='')),
                ('img', models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='')),
                ('quantity', models.IntegerField(default=1, verbose_name='')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='')),
                ('teh_desc', models.TextField(verbose_name='')),
                ('pay', models.TextField(verbose_name='')),
                ('delivary', models.TextField(verbose_name='')),
                ('category', models.ManyToManyField(to='app_shop.category', verbose_name='')),
                ('sub_category', models.ManyToManyField(to='app_shop.subcategory', verbose_name='')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
            },
        ),
    ]