# Generated by Django 4.0 on 2021-12-31 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0012_book_edition_alter_book_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='edition',
            field=models.SmallIntegerField(default=1),
        ),
    ]
