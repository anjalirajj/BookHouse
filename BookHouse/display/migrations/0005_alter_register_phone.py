# Generated by Django 4.0 on 2021-12-28 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0004_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='phone',
            field=models.IntegerField(default='0'),
        ),
    ]
