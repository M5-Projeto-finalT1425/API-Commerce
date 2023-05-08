from rest_framework import permissions
from rest_framework.views import View
from accounts.models import Account
from .models import Product


class IsAdminOrStaffOrCreate(permissions.BasePermission):
    def has_permission(self, request, view: View) -> bool:
        return (
            request.user.is_staff
            and request.method == "POST"
            or request.method == "GET"
        )


class StaffOrGET(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: Product) -> bool:
        return (
            request.user.is_staff
            and obj.seller == request.user
            or request.method == "GET"
            or request.user.is_superuser
        )
