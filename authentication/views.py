from django.shortcuts import redirect, render
from django.contrib.messages import add_message, constants
from authentication.models import User
from django.contrib.auth import login, logout,authenticate
from django.contrib import messages
from decorators import is_logged_in
# Create your views here.



def LoginView(request):
    user = None
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(request, username=u, password=p)
        if user is not None:
            login(request, user)
            # add_message(request, constants.SUCCESS, 'login success')
            return redirect('dashboard_view')
        else:
            messages.error(request, 'username or password not correct')
            return redirect('login_view')

    return render(request, 'login.html')

def Logout(request):
    logout(request)
    return redirect('dashboard_view')