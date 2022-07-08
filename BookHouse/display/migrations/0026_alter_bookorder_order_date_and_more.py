# Generated by Django 4.0 on 2022-01-18 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('display', '0025_cart_quantity_bookrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookorder',
            name='order_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='bookpayment',
            name='transaction_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='bookrequest',
            name='order_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='RoomPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0)),
                ('month', models.IntegerField()),
                ('start_date', models.DateField()),
                ('upto_date', models.DateField()),
                ('book_date', models.DateTimeField(auto_now_add=True)),
                ('seat_alloted', models.CharField(max_length=20)),
                ('payment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='display.bookpayment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]