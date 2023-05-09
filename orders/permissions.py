from rest_framework import permissions
from orders.models import Order


class IsStaffOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: Order):
        return (
            request.user.is_staff
            or request.user == obj.user
            or request.method == "PATCH"
            and request.user.is_staff
        )


class IsStaffOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff
