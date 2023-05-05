from rest_framework import generics 
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from .serializers import OrderSerializer
from .models import Order
from .permissions import IsOrderOwner, IsStaff
from products.models import Product

class OrderView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        serializer.save(account=self.request.user)

        product_ids = self.request.data.get('products', [])

        order = serializer.instance
        for product_id in product_ids:
            product = Product.objects.get(id=product_id)
            order.products.add(product)

class OrderDetailView(generics.RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOrderOwner | IsStaff]

    lookup_field = "id"
    lookup_url_kwarg = "order_id"

    def partial_update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsStaff]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Order.objects.all()
        else:
            return Order.objects.filter(account=self.request.user)


