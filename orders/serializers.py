from rest_framework import serializers
from .models import Order
from products.models import Product


class CustomDateTimeField(serializers.DateTimeField):
    def to_representation(self, value):
        return value.strftime("%Y-%m-%d %H:%M:%S")


class OrderSerializer(serializers.ModelSerializer):
    created_at = CustomDateTimeField(read_only=True)

    def create(self, validated_data: dict):
        for product in validated_data["products"]:
            product_obj = Product.objects.get(id=product["id"])
            product_obj.quantity = product_obj.quantity - 1
            product_obj.save()
            if product_obj.quantity == 0:
                product_obj.in_stock = False
                product_obj.save()

    def update(self, instance: Order, validated_data: dict) -> Order:
        for key, value in validated_data.items():
            setattr(instance, key, value)
            instance.save()

        return instance

    class Meta:
        model = Order
        fields = ["id", "status", "created_at", "user", "products"]
        read_only_fields = ["products", "user"]
