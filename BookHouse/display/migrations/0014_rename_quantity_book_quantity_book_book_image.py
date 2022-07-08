# Generated by Django 4.0 on 2021-12-31 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0013_alter_book_edition'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Quantity',
            new_name='quantity',
        ),
        migrations.AddField(
            model_name='book',
            name='book_image',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
