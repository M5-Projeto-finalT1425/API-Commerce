from django.db import models
from django.utils import timezone
from accounts.models import Account


class Order(models.Model):
    class Meta:
        ordering = ["id"]

    STATUS_CHOICES = (
        ("PEDIDO REALIZADO", "Realizado"),
        ("EM ANDAMENTO", "Andamento"),
        ("ENTREGUE", "Entregue"),
    )

    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="PEDIDO REALIZADO"
    )
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="orders")
    products = models.JSONField()
