from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import CartSerializer
from .permissions import IsOwnerOrAdmin
from products.models import Product
from .models import Cart
from drf_spectacular.utils import extend_schema


class CartUpdateDestroyView(UpdateAPIView, DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Product.objects.all()
    serializer_class = CartSerializer

    @extend_schema(
        operation_id="cart_update",
        responses={200: CartSerializer},
        description="Rota de Adição de produtos ao carrinho.",
        summary="Adicionar produtos ao carrinho.",
        tags=["Adicionar produtos ao carrinho."],
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    
    @extend_schema(
        operation_id="cart_delete",
        responses={204: CartSerializer},
        description="Rota de excluir produtos do carrinho.",
        summary="Excluir produtos do carrinho.",
        tags=["Excluir produtos do carrinho."],
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    
    @extend_schema(
        operation_id="cart_update",
        responses={200: CartSerializer},
        description="Rota de Adição de produtos ao carrinho.",
        summary="Adicionar produtos ao carrinho.",
        tags=["Adicionar produtos ao carrinho."],
        exclude=True
    )
    def put(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    def perform_update(self, serializer):
        return serializer.save(user=self.request.user)


class CartRetrieveView(RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrAdmin]

    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    @extend_schema(
        operation_id="cart_retrieve",
        responses={200: CartSerializer},
        description="Rota de Captura do carrinho.",
        summary="Vizualizar carrinho.",
        tags=["Vizualizar carrinho."],
    )
    def get(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
