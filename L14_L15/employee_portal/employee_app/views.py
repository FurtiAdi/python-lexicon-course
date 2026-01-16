from django.shortcuts import render
from django.contrib.auth.models import User
from employee_app.forms import EmployeeForm, EmployeeProfileInfoForm
# Create your views here.
def index(request):
    return render(request, 'employee_app/index.html')

def register(request):
    registered = False
    if request.method == "POST":
        employee_form = EmployeeForm(data=request.POST)
        profile_form = EmployeeProfileInfoForm(data=request.POST)

        if employee_form.is_valid() and profile_form.is_valid():
            employee = employee_form.save()
            employee.set_password(employee.password)
            employee.save()

            profile = profile_form.save(commit=False)
            profile.employee = employee

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            request.session['employee_id'] = employee.id #session variable to store employee id
            registered = True
        else:
            print(employee_form.errors, profile_form.errors)
    else:
        employee_form = EmployeeForm()
        profile_form = EmployeeProfileInfoForm()

    return render(request, 'employee_app/registration.html',
                  {'employee_form': employee_form,
                   'profile_form': profile_form,
                   'registered': registered})

def preview(request):
    registered = False
    if 'employee_id' in request.session:
        employee_id = request.session['employee_id']
        employee = User.objects.get(id=employee_id)
        registered = True
        return render(request, 'employee_app/preview.html', {'employee_username': employee.username,
                                                             'employee_email': employee.email,
                                                             'employee_linkedin_site': employee.employeeprofileinfo.linkedin_site,
                                                             'employee_profile_pic': employee.employeeprofileinfo.profile_pic,
                                                             'registered': registered})
