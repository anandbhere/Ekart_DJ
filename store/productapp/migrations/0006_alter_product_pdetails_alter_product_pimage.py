# Generated by Django 4.2.6 on 2023-10-26 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0005_product_pimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pdetails',
            field=models.CharField(max_length=100, verbose_name='Product Details'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pimage',
            field=models.ImageField(upload_to='appimage/product', verbose_name='Upload image to'),
        ),
    ]
