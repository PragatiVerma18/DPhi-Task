from rest_framework import permissions


class IsAuthenticatedAndBuyer(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user and request.user.role == "Buyer"


class IsAuthenticatedAndNursery(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user and request.user.role == "Nursery"
