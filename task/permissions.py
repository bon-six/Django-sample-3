from rest_framework import permissions

class IsManagerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # ready only is allowed for all user
        if request.method in permissions.SAFE_METHODS:
            return True

        # write permissions only for manager
        # compare two user object check if same
        return obj.manager == request.user

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # ready only is allowed for all user
        if request.method in permissions.SAFE_METHODS:
            return True

        # write permissions only for manager
        # compare two user object check if same
        return request.user.is_authenticated and request.user.is_admin

class IsManagerOrAuthenticated(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # ready only is allowed for all user
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated

        # write permissions only for manager
        # compare two user object check if same
        return obj.manager == request.user

class IsAdminOrAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        # ready only is allowed for all user
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated

        # write permissions only for manager
        # compare two user object check if same
        return request.user.is_authenticated and request.user.is_admin

class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_admin)

class IsManager(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_authenticated and (request.user == obj.manager))