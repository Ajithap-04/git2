# Generated by Django 5.0.1 on 2024-02-10 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapp', '0005_remove_orders_product_orders_cart_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='email',
            field=models.EmailField(default=2, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('cancelled', 'cancelled'), ('delivered', 'delivered'), ('order-placed', 'order-placed'), ('dispatched', 'dispatched')], default='order-placed', max_length=100),
        ),
    ]
