# Generated by Django 4.1.1 on 2022-10-18 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0004_alter_productcategory_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(max_length=6, unique=True, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='code',
            field=models.CharField(max_length=3, unique=True, verbose_name='Código'),
        ),
    ]
