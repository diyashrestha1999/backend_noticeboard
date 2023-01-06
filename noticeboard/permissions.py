from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        is_owner = obj.user == request.user

        if view.action == 'destroy':
            return request.user.is_superuser or is_owner

        return is_owner





