from rest_framework import serializers
from .models import Order

class CustomDateTimeField(serializers.DateTimeField):
    def to_representation(self, value):
        return value.strftime('%Y-%m-%d %H:%M:%S')

class OrderSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    created_at = CustomDateTimeField(read_only= True)

    def get_products(self, order):
        product_list = []
        for product in order.products.all():
            product_list.append({"name": product.name, "value": product.value, "category": product.category})
        return product_list

    class Meta:
        model = Order
        fields = '__all__'
