# Generated by Django 4.2 on 2023-05-08 17:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0003_product_category"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="account",
            new_name="seller",
        ),
    ]
