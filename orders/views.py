from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from products.serializers import ProductReturnSerializer, ProductSerializer
from .serializers import OrderSerializer
from .models import Order
from products.models import Product
from .permissions import IsStaffOrAdmin, IsStaffOrOwner
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
)
from django.db.models import Q
import ipdb


class OrderView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        cart_products = self.request.user.cart.products.all()
        product_serializer = ProductReturnSerializer(cart_products, many=True)
        products_data = product_serializer.data
        serializer.save(
            user=self.request.user,
            products=products_data,
            cart_prods=products_data,
        )

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderStaffView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsStaffOrAdmin]
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(
            products__contains=[{"seller": self.request.user.id}]
        )


class OrderDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsStaffOrOwner]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    lookup_url_kwarg = "order_id"
