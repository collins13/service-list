from functools import wraps
from django.shortcuts import redirect


def verified_user_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_verified:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('verified')
    return wrapper
