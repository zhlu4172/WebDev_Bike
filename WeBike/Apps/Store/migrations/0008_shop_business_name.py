# Generated by Django 4.1 on 2022-09-26 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0007_blog_self_written'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='Business_Name',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]