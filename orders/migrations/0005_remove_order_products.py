# Generated by Django 4.2 on 2023-05-08 13:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0004_order_products"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="products",
        ),
    ]