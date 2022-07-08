# Generated by Django 3.2.9 on 2021-12-27 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='name', max_length=50)),
                ('email', models.EmailField(default='email', max_length=50)),
                ('number', models.CharField(default='0', max_length=20)),
                ('message', models.CharField(default='message', max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='user_query',
        ),
    ]