from rest_framework import permissions
from rest_framework.views import View
from .models import Address


class IsAdminOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: Address) -> bool:
        return request.user.is_superuser or obj.account == request.user
