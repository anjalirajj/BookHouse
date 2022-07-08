# Generated by Django 4.0 on 2022-01-16 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('display', '0023_issued_status_bookpayment_bookorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(default='cart', max_length=50)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='display.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]