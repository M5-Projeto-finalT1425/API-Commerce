from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import ListCreateAPIView, UpdateAPIView
from .models import Cart
from .serializers import CartSerializer
from accounts.permissions import IsAdminOrOwner
from products.models import Product


class CartView(UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_class = [IsAdminOrOwner]

    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_url_kwarg = "product_id"

    def perform_update(self, serializer):
        product_instance = get_object_or_404(Product, pk=self.kwargs["product_id"])
        serializer.save(product_instance=product_instance)
