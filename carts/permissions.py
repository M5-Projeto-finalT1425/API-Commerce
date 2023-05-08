from rest_framework import permissions
from rest_framework.views import View
from .models import Cart


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: Cart) -> bool:
        return request.user.is_superuser or obj.user == request.user
