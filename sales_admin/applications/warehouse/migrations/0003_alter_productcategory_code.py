# Generated by Django 4.1.1 on 2022-10-18 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0002_remove_product_currency_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='code',
            field=models.CharField(max_length=6, unique=True, verbose_name='Código'),
        ),
    ]
