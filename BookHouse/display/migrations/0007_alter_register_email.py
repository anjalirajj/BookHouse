# Generated by Django 4.0 on 2021-12-28 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0006_alter_contact_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.EmailField(default='your mail', max_length=50),
        ),
    ]