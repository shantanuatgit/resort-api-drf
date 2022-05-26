from rest_framework import permissions

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
OBJECT_SAFE_METHODS = ()

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in SAFE_METHODS or request.user and request.user.is_staff)


class IsAdminOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_staff)


class IsOwnerOrAdminOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj ):
        admin_permission = bool(request.user and request.user.is_staff)
        if request.method in OBJECT_SAFE_METHODS:
            return True
        return obj.name == request.user or admin_permission


class IsOwnerOrManagerOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj ):
        manager_permission = bool(request.user and request.user.is_manager)
        if request.method in OBJECT_SAFE_METHODS:
            return True
        return obj.name == request.user or manager_permission


class IsManagerOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_manager)
