from django.db import models
from accounts.models import Account


class Product(models.Model):
    class Meta:
        ordering = ["id"]

    name = models.CharField(max_length=150)
    quantity = models.IntegerField(default=0)
    value = models.DecimalField(max_digits=6, decimal_places=2)
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name="products",
        null=True,
        blank=True,
    )
