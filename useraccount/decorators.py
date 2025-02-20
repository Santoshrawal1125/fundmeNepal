from django.contrib import messages
from django.shortcuts import redirect


def login_required(view_fun):
    def wrapper_fun(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_fun(request, *args, **kwargs)

        else:
            messages.warning(request, "Login Required...")
            return redirect('useraccount:login')

        return wrapper_fun
