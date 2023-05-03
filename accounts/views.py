from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Account
from .serializers import AccountSerializer
from .permissions import IsAdminOrCreate, IsAdminOrOwner


class AccountView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrCreate]

    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrOwner]

    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_url_kwarg = "account_id"
