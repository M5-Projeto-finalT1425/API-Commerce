from rest_framework_simplejwt.authentication import JWTAuthentication
from products.permissions import IsAdminOrStaffOrCreate
from rest_framework.generics import ListCreateAPIView
from .models import Product
from .serializers import ProductSerializer


class ProductView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrStaffOrCreate]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    ...
