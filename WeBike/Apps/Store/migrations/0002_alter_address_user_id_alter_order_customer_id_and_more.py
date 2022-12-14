# Generated by Django 4.1 on 2022-09-15 02:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='User_ID',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='Customer_ID',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='Product_ID',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Store.products'),
        ),
    ]
