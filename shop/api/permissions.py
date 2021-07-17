from rest_framework import permissions
from accounts.api.views import get_user_from_token


class NurseryPermission(permissions.BasePermission):
    """
    Reserve Routes for Nursery
    """

    def has_permission(self, request, view):
        get_user_from_token(self.request)
        if request.user.is_authenticated and request.user.role == "Buyer":
            if view.action == "retrieve" or view.action == "list":
                return request.user.has_perms("buyer_perm")
        if request.user.is_authenticated and request.user.role == "Nursery":
            if (
                view.action == "create"
                or view.action == "update"
                or view.action == "partial_update"
                or view.action == "destroy"
            ):
                return request.user.has_perms("nursery_perm")
        return True


class BuyerPermission(permissions.BasePermission):
    """
    Reserve Routes for Buyer
    """

    def has_permission(self, request, view):
        get_user_from_token(self.request)
        if request.user.is_authenticated and request.user.role == "Buyer":
            return request.user.has_perms("buyer_perm")
        return True
