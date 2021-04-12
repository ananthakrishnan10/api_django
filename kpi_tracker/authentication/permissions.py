from rest_framework.permissions import BasePermission

from .enumerations import UserRoleEnum


class IsStaffAccessible(BasePermission):
    def has_permission(self, request, view):
        if request.user.role.name == UserRoleEnum.staff.name:
            return True
        return False


class IsAdminAccessible(BasePermission):
    def has_permission(self, request, view):
        if request.user.role.name == UserRoleEnum.admin.name:
            return True
        return False
