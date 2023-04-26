from django.urls import path
from .views import LoginView, Logout

urlpatterns = [
    path('', LoginView, name='login_view'),
    path('logout/', Logout, name='logout_view'),

]