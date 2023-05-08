from rest_framework import permissions
from orders.models import Order


class IsStaffOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: Order):
        return (
            request.method == "POST"
            or request.user.is_staff
            or request.user == obj.user
        )
