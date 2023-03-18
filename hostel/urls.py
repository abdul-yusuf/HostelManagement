from django.urls import path 
from .views import *


urlpatterns = [
    path('', HomeView, name='home_view'),
    path('login', LoginView, name='login_view'),
    path('logout', Logout, name='logout_view'),
    path('dashboard', DashboardView, name='dashboard_view'),

]