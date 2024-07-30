from rest_framework import permissions


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        """
        Проверяет, является ли пользователь - владельцем привычки.
        """
        if obj.owner == request.user:
            return True
        return False