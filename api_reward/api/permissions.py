from rest_framework import permissions


class UserOrReadOnly(permissions.BasePermission):
    '''Custom permission,'''
    '''which gives full access to the object only to the author'''

    def has_permission(self, request, view):
        return (
                request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated
            )

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class AuthorOrReadOnly(permissions.BasePermission):
    '''Custom permission,'''
    '''which gives full access to the object only to the author'''

    def has_permission(self, request, view):
        return (
                request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated
            )

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
