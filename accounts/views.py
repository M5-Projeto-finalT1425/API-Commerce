from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Account
from .serializers import AccountSerializer
from .permissions import IsAdminOrCreate, IsAdminOrOwner
from drf_spectacular.utils import extend_schema


class AccountView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrCreate]

    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    @extend_schema(
        operation_id="account_list",
        responses={200: AccountSerializer},
        description="Rota de Listagem dos usuários.",
        summary="Listagem dos usuários.",
        tags=["Listagem dos usuários."],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @extend_schema(
        operation_id="account_create",
        responses={201: AccountSerializer},
        description="Rota de Criação de usuários",
        summary="Criação de usuários",
        tags=["Criação de usuários"],
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class AccountDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrOwner]

    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_url_kwarg = "account_id"

    @extend_schema(
        operation_id="account_retrieve",
        responses={200: AccountSerializer},
        description="Rota de Captura de usuário.",
        summary="Vizualizar usuário.",
        tags=["Vizualizar usuário."],
    )
    def get(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @extend_schema(
        operation_id="account_update",
        responses={200: AccountSerializer},
        description="Rota de Edição de usuário.",
        summary="Editar usuário.",
        tags=["Editar usuário."],
        exclude=["PUT"],
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    
    @extend_schema(
        operation_id="account_delete",
        responses={204: AccountSerializer},
        description="Rota de Remoção de usuário.",
        summary="Excluir usuário.",
        tags=["Excluir usuário."],
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    
    @extend_schema(
        operation_id="account_update",
        responses={200: AccountSerializer},
        description="Rota de Edição de usuário.",
        summary="Edição de usuário.",
        tags=["Edição de usuário."],
        exclude=True,
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    
    