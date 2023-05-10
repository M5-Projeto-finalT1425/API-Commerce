from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Address
from .serializers import AddressSerializer
from .permissions import IsAdminOrOwner
from drf_spectacular.utils import extend_schema


class AddressView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrOwner]

    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    @extend_schema(
        operation_id="address_create",
        responses={201: AddressSerializer},
        description="Rota de Criação de Endereço.",
        summary="Criação de Endereço.",
        tags=["Criação de Endereço."],
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    


class AddressDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrOwner]

    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    lookup_url_kwarg = "address_id"

    @extend_schema(
        operation_id="address_retrieve",
        responses={200: AddressSerializer},
        description="Rota de Captura do Endereço.",
        summary="Vizualizar Endereço.",
        tags=["Vizualizar Endereço."],
    )
    def get(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @extend_schema(
        operation_id="address_update",
        responses={200: AddressSerializer},
        description="Rota de Edição do Endereço.",
        summary="Editar Endereço.",
        tags=["Editar Endereço."],
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    
    @extend_schema(
        operation_id="address_create",
        responses={204: AddressSerializer},
        description="Rota de Remoção do Endereço.",
        summary="Excluir Endereço.",
        tags=["Excluir Endereço."],
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    
    @extend_schema(
        operation_id="address_update",
        responses={200: AddressSerializer},
        description="Rota de Edição do Endereço.",
        summary="Edição do Endereço.",
        tags=["Edição do Endereço."],
        exclude=True
    )
    def put(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
