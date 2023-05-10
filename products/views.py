from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from products.permissions import IsAdminOrStaffOrCreate, StaffOrGET
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Product
from .serializers import ProductSerializer
from drf_spectacular.utils import extend_schema


class ProductView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrStaffOrCreate]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ("id", "name", "category")

    @extend_schema(
        operation_id="product_list",
        responses={200: ProductSerializer},
        description="Rota de listagem de produtos.",
        summary="Listagem dos produtos.",
        tags=["Listagem dos produtos."],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @extend_schema(
        operation_id="product_create",
        responses={201: ProductSerializer},
        description="Rota de Criação de produtos.",
        summary="Criação de produtos.",
        tags=["Criação de produtos."],
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        return serializer.save(seller=self.request.user)


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [StaffOrGET]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = "product_id"

    @extend_schema(
        operation_id="address_retrieve",
        responses={200: ProductSerializer},
        description="Rota de Captura de Produtos.",
        summary="Vizualizar Produto.",
        tags=["Vizualizar Produto."],
    )
    def get(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @extend_schema(
        operation_id="address_update",
        responses={200: ProductSerializer},
        description="Rota de Edição de Produtos.",
        summary="Editar Produtos.",
        tags=["Editar Produtos."],
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    
    @extend_schema(
        operation_id="address_create",
        responses={204: ProductSerializer},
        description="Rota de Remoção de Produtos.",
        summary="Excluir Produtos.",
        tags=["Excluir Produtos."],
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    
    @extend_schema(
        operation_id="address_update",
        responses={200: ProductSerializer},
        description="Rota de Edição de Produtos.",
        summary="Edição de Produtos.",
        tags=["Edição de Produtos."],
        exclude=True
    )
    def put(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

