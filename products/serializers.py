from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "quantity", "value", "category", "seller", "in_stock"]
        read_only_fields = ["in_stock"]
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


class ProductReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "value", "category", "seller"]
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
