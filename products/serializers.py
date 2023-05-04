from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "quantity", "value", "account"]
        extra_kwargs = {
            "name": {
                "validators": [
                    UniqueValidator(
                        queryset=Product.objects.all(),
                        message="A product with that name already exists.",
                    )
                ]
            },
        }
