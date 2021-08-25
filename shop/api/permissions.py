from rest_framework import permissions
from accounts.api.views import get_user_from_token


class IsAuthenticatedAndBuyer(BasePermission):

    """
    Reserve Routes for Buyer
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == "Buyer"

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user and request.user.role == "Buyer"


class IsAuthenticatedAndNursery(BasePermission):

    """
    Reserve Routes for Nursery
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == "Nursery"

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user and request.user.role == "Nursery"
