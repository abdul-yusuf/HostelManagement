from django.shortcuts import redirect, render
from django.contrib.messages import add_message, constants
from authentication.models import User
from django.contrib.auth import login, logout,authenticate

from decorators import is_logged_in
# Create your views here.


def Login(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(request, username=u, password=p)
        if user is not None:
            login(request, user)
            if user.is_student:
                print('you are directed to student page')
            else:
                pass
            # add_message(request, constants.SUCCESS, 'login success')
            # if user.is_kitchen: return redirect('kitchen:dashboard')
            # elif user.is_admin: return redirect('administrator:dashboard')
            # return redirect('restaurant:dashboard')
        # add_message(request, constants.ERROR, 'Invalid credentials')
    return render(request, 'authentication/login.html')

def LogOut(request):
    logout(request)
    return redirect('restaurant:welcome')