# Generated by Django 4.1 on 2022-09-23 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0006_remove_products_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='Self_Written',
            field=models.BooleanField(default=False),
        ),
    ]