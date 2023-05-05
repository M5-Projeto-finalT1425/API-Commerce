from django.db import models


class Cart(models.Model):
    account = models.OneToOneField(
        "accounts.Account",
        on_delete=models.CASCADE,
        related_name="cart",
        null=True,
        blank=True,
    )
    products = models.ManyToManyField("products.Product", related_name="carts")
