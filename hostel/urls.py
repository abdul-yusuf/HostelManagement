from django.urls import path 
from .views import *


urlpatterns = [
    path('', HomeView, name='home_view'),
    # path('login/', LoginView, name='login_view'),
    path('report/', ReportView, name='report_view'),
    path('report_list/', ReportListView, name='report_list_view'),
    path('close_report/<int:id>/', CloseReport, name='close_report_view'),
    path('dashboard/', DashboardView, name='dashboard_view'),
    path('user_list/<str:categ>/', StudentListView, name='student_list_view'),
]