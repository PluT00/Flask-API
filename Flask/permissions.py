from rest_framework import permissions


class IsMember(permissions.BasePermission):
    """
    Object-level permission to only allow member of an object see it.
    Assumes the model instance has an `member` attribute.
    """

    def has_object_permission(self, request, view, obj):
        return request.user in obj.members.all()


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow author of an object edit it.
    Assumes the model instance has an `author` attribute.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user == obj.author
