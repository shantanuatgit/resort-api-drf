from rest_framework import permissions

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, views):
        return bool(request.method in SAFE_METHODS or request.user and request.user.is_staff)


class AdminOnly(permissions.BasePermission):
    def has_permission(self, request, views):
        return bool(request.user.is_staff)
