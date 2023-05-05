from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .serializers import CartSerializer
from accounts.permissions import IsAdminOrOwner
from products.models import Product


class CartView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_class = [IsAdminOrOwner]

    queryset = Product.objects.all()
    serializer_class = CartSerializer

    def perform_update(self, serializer):
        return serializer.save(user=self.request.user)
