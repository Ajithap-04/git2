# Generated by Django 5.0.1 on 2024-02-10 06:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommapp', '0004_orders'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='product',
        ),
        migrations.AddField(
            model_name='orders',
            name='cart',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='ecommapp.carts'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('cancelled', 'cancelled'), ('dispatched', 'dispatched'), ('delivered', 'delivered'), ('order-placed', 'order-placed')], default='order-placed', max_length=100),
        ),
    ]
