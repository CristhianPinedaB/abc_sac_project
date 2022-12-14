# Generated by Django 4.1.1 on 2022-10-22 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_alter_client_address_alter_client_document_number_and_more'),
        ('sales', '0007_remove_orderitem_order_order_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.ForeignKey(db_column='client_id', default=None, on_delete=django.db.models.deletion.CASCADE, related_name='client_order', to='crm.client', verbose_name='Cliente'),
        ),
    ]
