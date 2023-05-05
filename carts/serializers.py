from rest_framework import serializers
from .models import Cart
from django.shortcuts import get_object_or_404
from products.serializers import ProductSerializer


class CartSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    def update(self, instance, validated_data):
        user = validated_data.pop("user")
        cart = get_object_or_404(Cart, id=user.cart.id)
        cart.products.add(instance)
        return cart

    class Meta:
        model = Cart
        fields = ["id", "account", "products"]
