# Generated by Django 4.0 on 2022-01-16 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0021_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(default='image/user.png', upload_to='profile_image/'),
        ),
    ]
