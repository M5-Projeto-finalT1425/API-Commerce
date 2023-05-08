from rest_framework_simplejwt.authentication import JWTAuthentication
from products.serializers import ProductReturnSerializer
from .serializers import OrderSerializer
from .models import Order
from .permissions import IsStaffOrOwner
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)


class OrderView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsStaffOrOwner]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        cart_products = self.request.user.cart.products.all()
        product_serializer = ProductReturnSerializer(cart_products, many=True)
        products_data = product_serializer.data
        serializer.save(
            user=self.request.user,
            products=products_data,
        )

    def get_queryset(self):
        if self.request.user.is_staff:
            return Order.objects.all()
        else:
            return Order.objects.filter(account=self.request.user)


class OrderDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsStaffOrOwner]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    lookup_url_kwarg = "order_id"
