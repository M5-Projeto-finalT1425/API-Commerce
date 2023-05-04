from rest_framework import permissions
from rest_framework.views import View


class IsAdminOrStaffOrCreate(permissions.BasePermission):
    def has_permission(self, request, view: View) -> bool:
        return (
            request.user.is_staff
            and request.method == "POST"
            or request.method == "GET"
        )


class StaffOrGET(permissions.BasePermission):
    def has_permission(self, request, view: View) -> bool:
        return (
            request.user.is_staff
            and request.method == "PATCH"
            and request.method == "PUT"
            and request.method == "DELETE"
            or request.method == "GET"
        )
