# Generated by Django 4.0 on 2022-01-01 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0014_rename_quantity_book_quantity_book_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_image',
            field=models.ImageField(default='', upload_to='images/book_images'),
        ),
    ]