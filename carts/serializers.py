from rest_framework import serializers
from .models import Cart
import ipdb


class CartSerializer(serializers.ModelSerializer):
    def update(self, validated_data):
        product_instance = validated_data.pop("product_instance")
        cart = validated_data.account.cart
        ipdb.set_trace()
        return cart.product.add(product_instance)

    class Meta:
        model = Cart
        fields = ["id", "account", "products"]
