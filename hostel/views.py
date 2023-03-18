from django.shortcuts import render, redirect
from .models import *
from authentication.models import User 
from complaints.models import Complaint, Response
from django.contrib.auth import login, logout,authenticate
from django.contrib.messages import add_message, constants


# Create your views here.

def HomeView(request):
    return render(request, 'login.html')

def LoginView(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(request, username=u, password=p)
    if user is not None:
        login(request, user)
        add_message(request, constants.SUCCESS, 'login success')
        return redirect('hostel:dashboard_view')
    add_message(request, constants.ERROR, 'Invalid credentials')
# return render(request, 'authentication/login.html')

    return render(request, 'login.html')

def Logout(request):
    return render(request, 'login.html')

def DashboardView(request):
    context = {
        'user':request.user,
    }
    return render(request, 'search.html', context)

def StudentListView(request):
    context = {
        'students': User.objects.filter(is_student=True)
    }
    return render(request, 'search.html', context)

def ReportView(request):
    return render(request, 'search.html')

def ReportListView(request):
    context = {
        'reports':Complaint.objects.all()
    }
    return render(request, 'search.html', context)
