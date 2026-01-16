from django import forms
from django.contrib.auth.models import User
from employee_app.models import EmployeeProfileInfo


class EmployeeForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class EmployeeProfileInfoForm(forms.ModelForm):
    class Meta():
        model = EmployeeProfileInfo
        fields = ('linkedin_site', 'profile_pic')
