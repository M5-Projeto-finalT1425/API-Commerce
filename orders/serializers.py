from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from products.models import Product
from .email import send_email_order
from products.serializers import ProductReturnSerializer
import ipdb


class CustomDateTimeField(serializers.DateTimeField):
    def to_representation(self, value):
        return value.strftime("%Y-%m-%d %H:%M:%S")


class OrderSerializer(serializers.ModelSerializer):
    created_at = CustomDateTimeField(read_only=True)

    def create(self, validated_data: dict):
        sellers_lst = []
        orders = []

        cart_products = validated_data.pop("cart_prods")
        for product in cart_products:
            product_obj = Product.objects.get(id=product["id"])
            if product_obj.quantity > 0:
                product_obj.quantity -= 1
                product_obj.save()
            if product_obj.quantity == 0:
                product_obj.in_stock = False
                product_obj.save()

            seller = product_obj.seller
            seller_count = sellers_lst.count(seller)
            if seller_count == 0:
                sellers_lst.append(seller)
                find_seller_products = [
                    prod for prod in cart_products if prod["seller"] == seller.id
                ]
                validated_data["products"] = find_seller_products
                order = Order.objects.create(**validated_data)
                orders.append(order)

        return orders

    def update(self, instance: Order, validated_data: dict) -> Order:
        for key, value in validated_data.items():
            setattr(instance, key, value)
            instance.save()
            send_email_order(instance)
        return instance

    class Meta:
        model = Order
        fields = ["id", "status", "created_at", "user", "products"]
        read_only_fields = ["products", "user"]
