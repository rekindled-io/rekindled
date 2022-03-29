from rest_framework import permissions


class AnonymousCreateAndOwnerUpdate(permissions.BasePermission):
    """
    - Allow POST by anonymous users
    - Allow PUT/PATCH for own records
    """

    def has_permission(self, request, view):
        return view.action == "create" or (
            request.user and request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return view.action in ["update", "partial_update"] and (
            obj.id == request.user.id or request.user.is_staff
        )
