from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import CartSerializer
from .permissions import IsOwnerOrAdmin
from products.models import Product
from .models import Cart


class CartUpdateDestroyView(UpdateAPIView, DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Product.objects.all()
    serializer_class = CartSerializer

    def perform_update(self, serializer):
        return serializer.save(user=self.request.user)


class CartRetrieveView(RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrAdmin]

    queryset = Cart.objects.all()
    serializer_class = CartSerializer
