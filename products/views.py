from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from products.permissions import IsAdminOrStaffOrCreate
from rest_framework.generics import ListCreateAPIView
from .models import Product
from .serializers import ProductSerializer


class ProductView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrStaffOrCreate]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        return serializer.save(account=self.request.user)

    ...
