from functools import wraps
from django.shortcuts import redirect

def is_login(func):
    @wraps(func)
    def wrap(request, *args, **kwargs):
        user = request.user

        if user.is_authenticated:
            if user.is_student:
                print('user is student')
            elif user.is_worker:
                print('user is worker')
            else:
                print('user is admin')
        else:
            func(request,*args, **kwargs)
    return wrap

def admin_only(func):
    @wraps(func)
    def wrap(request,*args, **kwargs):
        user = request.user

        if user.is_admin:
            print('access granted')
        else:
            print(f'{user.name} you have no access to this page')

    return wrap

def workers_only(func):
    @wraps(func)
    def wrap(request,*args, **kwargs):
        user = request.user

        if user.is_worker:
            print('access granted')
        else:
            print(f'{user.name} you have no access to this page')

    return wrap