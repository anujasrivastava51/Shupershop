# Generated by Django 4.2.2 on 2023-09-08 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0009_wishlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('orderStatus', models.IntegerField(choices=[(0, 'Order is Placed'), (1, 'Order is Packed'), (2, 'Ready to Dispatch'), (3, 'Dispatched'), (4, 'Out for Delivery'), (5, 'Delivered')], default=0)),
                ('paymentStatus', models.IntegerField(choices=[(0, 'Pending'), (1, 'Done')], default=0)),
                ('paymentMode', models.IntegerField(choices=[(0, 'COD'), (1, 'NetBanking')], default=0)),
                ('subtotal', models.IntegerField()),
                ('shipping', models.IntegerField()),
                ('total', models.IntegerField()),
                ('rppid', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.buyer')),
            ],
        ),
        migrations.CreateModel(
            name='CheckoutProduct',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('qty', models.IntegerField()),
                ('total', models.IntegerField()),
                ('checkout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.checkout')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.product')),
            ],
        ),
    ]
