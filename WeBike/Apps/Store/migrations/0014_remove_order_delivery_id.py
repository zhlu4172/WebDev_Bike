# Generated by Django 4.1 on 2022-10-10 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0013_order_address_order_city_order_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='Delivery_ID',
        ),
    ]
