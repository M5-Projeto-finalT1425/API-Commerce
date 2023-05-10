from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from products.serializers import ProductReturnSerializer
from .serializers import OrderSerializer
from .models import Order
from .permissions import IsStaffOrAdmin, IsStaffOrOwner
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
)
from django.db.models import Q
from drf_spectacular.utils import extend_schema


class OrderView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    queryset = Order

    @extend_schema(
        operation_id="order_list",
        responses={200: OrderSerializer},
        description="Rota de Listagem dos pedidos comprados.",
        summary="Listagem dos pedidos comprados.",
        tags=["Listagem dos pedidos comprados."],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @extend_schema(
        operation_id="order_create",
        responses={201: OrderSerializer},
        description="Rota de Criação dos pedidos.",
        summary="Criação dos pedidos.",
        tags=["Criação dos pedidos."],
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

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
    queryset = Order.objects.all()

    @extend_schema(
        operation_id="order_list_sold",
        responses={200: OrderSerializer},
        description="Rota de Listagem dos pedidos vendidos.",
        summary="Listagem dos pedidos vendidos.",
        tags=["Listagem dos pedidos vendidos."],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

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

    @extend_schema(
        operation_id="order_retrieve",
        responses={200: OrderSerializer},
        description="Rota de Vizualização do pedido.",
        summary="Vizualizar pedido.",
        tags=["Vizualizar pedido."],
    )
    def get(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @extend_schema(
        operation_id="order_update",
        responses={200: OrderSerializer},
        description="Rota de edição de status do pedido.",
        summary="Alterar status do pedido.",
        tags=["Alterar status do pedido."],
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    
    @extend_schema(
        operation_id="order_delete",
        responses={204: OrderSerializer},
        description="Rota de excluir o pedido.",
        summary="Excluir pedido.",
        tags=["Excluir pedido."],
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    
    @extend_schema(
        operation_id="order_update",
        responses={200: OrderSerializer},
        description="Rota de edição de status do pedido.",
        summary="Alterar status do pedido.",
        tags=["Alterar status do pedido."],
        exclude=True
    )
    def put(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

