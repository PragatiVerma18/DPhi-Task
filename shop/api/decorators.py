from django.core.exceptions import PermissionDenied


def user_is_nursery(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        if user.role == "Nursery":
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap


def user_is_buyer(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        if user.role == "Buyer":
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap
