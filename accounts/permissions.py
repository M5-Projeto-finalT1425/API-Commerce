from rest_framework import permissions
from rest_framework.views import View
from .models import Account


class IsAdminOrCreate(permissions.BasePermission):
    def has_permission(self, request, view: View) -> bool:
        return request.user.is_superuser or request.method == "POST"


class IsAdminOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: Account) -> bool:
        return request.user.is_superuser or obj == request.user
