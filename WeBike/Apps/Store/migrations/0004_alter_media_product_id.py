# Generated by Django 4.1 on 2022-09-15 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0003_alter_media_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='Product_ID',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Store.products'),
        ),
    ]
