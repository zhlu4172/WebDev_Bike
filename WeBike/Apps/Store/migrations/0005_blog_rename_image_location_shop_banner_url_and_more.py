# Generated by Django 4.1 on 2022-09-15 02:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0004_alter_media_product_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Blog_ID', models.PositiveIntegerField(unique=True)),
                ('Title', models.CharField(default='', max_length=255)),
                ('Preview', models.CharField(default='', max_length=255)),
                ('Image_URL', models.CharField(default='', max_length=255)),
                ('Blog_URL', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='shop',
            old_name='Image_Location',
            new_name='Banner_URL',
        ),
        migrations.AddField(
            model_name='order',
            name='Rent_end',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='Rent_start',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='Description',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='shop',
            name='Logo_URL',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='Product_Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(default='', max_length=255)),
                ('Age_Range', models.CharField(default='', max_length=255)),
                ('Brand', models.CharField(default='', max_length=255)),
                ('Speeds', models.PositiveIntegerField(blank=True, null=True)),
                ('Colour', models.CharField(default='', max_length=255)),
                ('Product_ID', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Store.products')),
            ],
        ),
    ]
