from django.shortcuts import render, redirect
from .models import *
from authentication.models import User
from complaints.models import Complaint, Response
from django.contrib.auth import login, logout, authenticate
from django.contrib.messages import add_message, constants
from decorators import is_logged_in, admin_only, staff_only
from django.contrib import messages

# Create your views here.

def HomeView(request):
    """
    A view that displays the homepage of your hostel management
    system. This could include information about the hostel, news and updates, and links to
    other pages on the site.
    """
    # print(dir(request))

    return render(request, 'login.html')
    # return redirect('login_view')




# @is_logged_in
def DashboardView(request):
    """
    A view that displays a dashboard for the user, showing information
    relevant to their role and permissions.
    """
    context = {
        'user': request.user,
    }
    return render(request, 'test_1.html')


# @admin_only
def StudentListView(request, categ):
    """
    A view that displays a list of all the staff members working at the hostel,
    including their names, roles, and contact information.
    """
    print(categ)
    if request.method == 'POST':
        # category = request.POST.get('category')
        category = categ
        username = request.POST.get('username')
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')

        try:
            fullname = fullname.split(' ')
            first_name = fullname[0]
            last_name = fullname[1],
        except IndexError:
            first_name = fullname
            last_name = ''
        print(fullname,fullname[1],first_name,last_name)
        new_user = User.objects.create_user(
            username=username,
            password= f'1234+{username}',

            first_name=first_name,
            last_name=last_name,
            email=email,
            is_student=True if category=='student' else False,
            is_staff=True if category=='staff' else False,
            is_worker=True if category=='worker' else False,
            is_admin=True if category=='admin' else False,
        )
        print(new_user)
        new_user.save()


    context = {
        'page_name': categ.capitalize(),
        'users': User.objects.filter(
            is_student=True if categ=='student' else False,
            is_worker=True if categ == 'worker' else False,
            is_staff=True if categ == 'Staff' else False,
        )
    }
    print(context)

    return render(request, 'test_2.html', context=context)

# def StaffListView(request):


# @is_logged_in
def ReportView(request):
    """
    A view that handles the submission of issue reports.
    This view should validate the form data, create a new IssueReport object in the
    database, and redirect the user to a confirmation page.

    A view that displays a form for submitting issue reports. This
    view can be accessed by students and staff members and should include fields for the
    following information:
    ● The name of the person submitting the report
    ● The type of issue (e.g. maintenance, security, noise)
    ● A description of the issue    including their names, roles, and contact information.
    ● The location of the issue (e.g. room number, common area)
    """
    if request.method=='POST':
        user = request.user
        complaint_type = request.POST.get('type')
        description = request.POST.get('discription')
        location = request.POST.get('location')
        print(complaint_type)
        new_complaint = Complaint.objects.create(
            user=user,
            massage=description,
            type=complaint_type,
        )
        new_complaint.save()
        messages.success(request, 'Report posted succesfully')

    return redirect('report_list_view')


# @staff_only
def ReportListView(request):
    """
    A view that displays a list of all the issue reports that have been
    submitted. This view can only be accessed by staff members and should display the
    following information for each issue report:

    ●The name of the person who submitted the report
    ●Additional explanation on the report
    ●The type of issue
    ●The date and time the report was submitted
    ●The status of the report (e.g. open, closed)
    """
    if request.method=='POST':
        obj_instance = Complaint.objects.get(pk=id)
        obj_instance.is_solved = True
        obj_instance.save()

    context = {
        'reports': Complaint.objects.all()
    }
    return render(request, 'complaint.html', context)

def CloseReport(request, id):
    obj_inst = Complaint.objects.get(pk=id)
    obj_inst.is_closed = True
    obj_inst.save()

    messages.success(request, 'Report Close Successfull')

    return redirect('report_list_view')
