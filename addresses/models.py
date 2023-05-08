from django.db import models
from accounts.models import Account


class Address(models.Model):
    class Meta:
        ordering = ["id"]

    city = models.CharField(max_length=50)
    street = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    number = models.CharField(max_length=3)
    user = models.OneToOneField(
        Account, on_delete=models.CASCADE, null=True, blank=True
    )
